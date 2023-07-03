"""
This module contains the unit test cases for utils.py
"""
import os
import pytest
import logging
from django.http import JsonResponse
from django.test import RequestFactory
from market_summary.utils import authenicate_token

@pytest.fixture
def request_factory():
    """
    Fixture for creating a request factory object
    """
    return RequestFactory()

def mock_exception(*args, **kwargs):
    """
    Mock function for raising exception
    """
    raise Exception('Mocked Exception')

@authenicate_token
def dummy_view(request):
    """
    Dummy view for testing decorator
    """
    return JsonResponse({"message": "Success"}, status=200)

@pytest.mark.parametrize(('api_key', 'status_code'), [('1234', 401), (os.environ.get('CLIENT_KEY'), 200)])
def test_authenicate_token(request_factory, api_key, status_code):
    """
    Test case for authenicate_token decorator
    """
    request = request_factory.get('/test_view', HTTP_API_KEY= api_key)
    response = dummy_view(request)
    assert response.status_code == status_code

def test_authenicate_token_exception(request_factory, monkeypatch):
    """
    Exception test case for authenicate_token decorator
    """
    monkeypatch.setattr(logging, 'info', mock_exception)
    request = request_factory.get('/test_view', HTTP_API_KEY= os.environ.get('CLIENT_KEY'))
    response = dummy_view(request)
    assert response.status_code == 500


import os
import pytest
from django.http import JsonResponse
from django.test import RequestFactory
from market_summary.utils import authenicate_token
import logging

@pytest.fixture
def request_factory():
    return RequestFactory()

def mock_exception(*args, **kwargs):
    raise Exception('Mocked Exception')

@authenicate_token
def dummy_view(request):
    return JsonResponse({"message": "Success"}, status=200)

@pytest.mark.parametrize(('API_KEY', 'status_code'), [('1234', 401), (os.environ.get('CLIENT_KEY'), 200)])
def test_authenicate_token(request_factory, API_KEY, status_code):
    request = request_factory.get('/test_view', HTTP_API_KEY= API_KEY)
    response = dummy_view(request)
    assert response.status_code == status_code

def test_authenicate_token_exception(request_factory, monkeypatch):
    monkeypatch.setattr(logging, 'info', mock_exception)
    request = request_factory.get('/test_view', HTTP_API_KEY= os.environ.get('CLIENT_KEY'))
    response = dummy_view(request)
    assert response.status_code == 500


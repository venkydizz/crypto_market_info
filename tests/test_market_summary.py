import os
import pytest
from django.test import Client
from django.urls import reverse
from market_summary import __version__
from config.common_config import COMMON_RESPONSE
import requests

@pytest.fixture
def client():
    return Client()

def mock_exception(*args, **kwargs):
    raise Exception('Mocked Exception')

def test_ping(client):
    url = reverse('ping')
    response = client.get(url)
    assert response.status_code == 200

def test_version(client):
    url = reverse('version')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == {"version": __version__}

@pytest.mark.parametrize('url_name', ['market_summary_all', 'market_summary_for'])
def test_invalid_auth(client, url_name):
    url = reverse(url_name)
    response = client.get(url, HTTP_API_KEY='1234')
    assert response.status_code == 401
    assert response.json() == COMMON_RESPONSE['401']

@pytest.mark.parametrize('url_name', ['market_summary_all', 'market_summary_for'])
def test_method_not_allowed(client, url_name):
    url = reverse(url_name)
    response = client.post(url, HTTP_API_KEY=os.environ.get('CLIENT_KEY'))
    assert response.status_code == 405
    assert response.json() == COMMON_RESPONSE['405']

def test_market_summary_all_success(client):
    url = reverse('market_summary_all')
    response = client.get(url, HTTP_API_KEY=os.environ.get('CLIENT_KEY'))
    assert response.status_code == 200

def test_market_summary_for_success(client):
    url = reverse('market_summary_for')
    response = client.get(url, {'market': '1ECO-BTC'}, HTTP_API_KEY=os.environ.get('CLIENT_KEY'))
    assert response.status_code == 200

def test_market_summary_for_missing_market(client):
    url = reverse('market_summary_for')
    response = client.get(url, HTTP_API_KEY=os.environ.get('CLIENT_KEY'))
    assert response.status_code == 400

@pytest.mark.parametrize('url_name', ['market_summary_all', 'market_summary_for'])
def test_exception(client, url_name, monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_exception)
    url = reverse(url_name)
    response = client.get(url,{'market': '1ECO-BTC'}, HTTP_API_KEY=os.environ.get('CLIENT_KEY'))
    assert response.status_code == 500
    assert response.json() == COMMON_RESPONSE['500']

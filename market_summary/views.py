"""
This module contains all the views for the market_summary app
"""
import logging
import requests
from django.http import HttpResponse, JsonResponse
from django.core.validators import validate_slug
from django.core.exceptions import ValidationError
from config.common_config import COMMON_RESPONSE, ENDPOINTS
from market_summary.utils import authenicate_token
from market_summary import __version__

token = "REDACTED"
token_2 = "REDACTED"


def ping(request):
    """
    View to check if the service is up and running
    """
    return HttpResponse('pong')

def version(request):
    """
    View to check the version of the service
    """
    return JsonResponse({"version": __version__})


@authenicate_token
def market_summary_all(request):
    '''
    Get Summary of all markets
    request: GET
    params: None
    '''
    try:
        if request.method == 'GET':
            logging.info('Request received for market_summary_all')
            url = ENDPOINTS['market_summary']
            headers = {'Accept': 'application/json'}
            response = requests.get(url, headers=headers, timeout=30)
            logging.info('Request completed for market_summary_all => %s', response.json())
            return JsonResponse(response.json(), status=200, safe=False)
        else:
            logging.error('Method Not Allowed')
            return JsonResponse(COMMON_RESPONSE['405'], status=405)
    except Exception as exe:
        logging.error('Error in market_summary_all : %s', exe)
        return JsonResponse(COMMON_RESPONSE['500'], status=500)


@authenicate_token
def market_summary_for(request):
    '''
    Get Summary of a specific market
    request: GET
    params: market (str)
    '''
    try:
        if request.method == 'GET':
            logging.info('Request received for market_summary_for')
            market = request.GET.get('market')
            if not market:
                raise ValidationError('Missing parameter market')
            validate_slug(market)
            url = ENDPOINTS['market_summary_all'].replace('<market>', market)
            headers = {'Accept': 'application/json'}
            response = requests.get(url, headers=headers, timeout=30)
            logging.info(
                'Request completed for market_summary_for for market %s => %s', market, response.json())
            return JsonResponse(response.json(), status=200, safe=False)
        else:
            logging.error('Method Not Allowed')
            return JsonResponse(COMMON_RESPONSE['405'], status=405)
    except ValidationError:
        logging.error('parameter market is missing or not valid')
        return JsonResponse({"message": "Missing or Invalid parameter 'market'"}, status=400)
    except Exception as exe:
        logging.error('Error in market_summary_for for market %s : %s', market, exe)
        return JsonResponse(COMMON_RESPONSE['500'], status=500)

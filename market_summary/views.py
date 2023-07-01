from django.http import HttpResponse, JsonResponse
import requests
import logging
from django.core.validators import validate_slug
from django.core.exceptions import ValidationError
from config.common_config import COMMON_RESPONSE, ENDPOINTS
from market_summary.utils import authenicate_token
from market_summary import __version__


def ping(request):
    # Service health check
    return HttpResponse('pong')

def version(request):
    # Service version
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
            response = requests.get(url, headers=headers)
            logging.info(f'Request completed for market_summary_all => {response.json()}')
            return JsonResponse(response.json(), status=200, safe=False)
        else:
            logging.error('Method Not Allowed')
            return JsonResponse(COMMON_RESPONSE['405'], status=405)
    except Exception as e:
        logging.error('Error in market_summary_all', str(e))
        return JsonResponse(COMMON_RESPONSE['500'], status=500)


@authenicate_token
def market_summary_for(request):
    '''
    Get Summary of a specific market
    request: GET
    params: market (str)
    '''
    if request.method == 'GET':
        try:
            logging.info('Request received for market_summary_for')
            market = request.GET.get('market')
            if not market:
                raise ValidationError('Missing parameter market')
            validate_slug(market)
            url = ENDPOINTS['market_summary_all'].replace('<market>', market)
            headers = {'Accept': 'application/json'}
            response = requests.get(url, headers=headers)
            logging.info(f'Request completed for market_summary_for for market {market} => {response.json()}')
            return JsonResponse(response.json(), status=200, safe=False)
        except ValidationError:
            logging.error('parameter market is missing or not valid')
            return JsonResponse({"message": "Missing or Invalid parameter 'market'"}, status=400)
        except Exception as e:
            logging.error(f'Error in market_summary_for for market {market}', str(e))
            return JsonResponse(COMMON_RESPONSE['500'], status=500)
    else:
        logging.error('Method Not Allowed')
        return JsonResponse(COMMON_RESPONSE['405'], status=405)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import logging
from config.common_config import BITTREX_URL, BITTREX_KEY, CLIENT_KEY

# Create your views here.
def ping(request):
    # Service health check
    return HttpResponse('pong')

def market_summary_all(request):
    '''
    Get Summary of all markets
    request: GET
    params: None
    '''
    if request.method == 'GET':
        try:
            logging.info('Request received for market_summary_all')
            api_key = request.META.get('HTTP_API_KEY')
            if api_key != CLIENT_KEY:
                logging.error('Unauthorized Request')
                return JsonResponse({"message": "Unauthorized Request"}, status=401)
            url = f'{BITTREX_URL}markets/summaries'
            headers = {'Accept': 'application/json', 'Apikey': BITTREX_KEY}
            response = requests.get(url, headers=headers)
            logging.info(f'Request completed for market_summary_all => {response.json()}')
            return JsonResponse(response.json(), status=200, safe=False)
        except Exception as e:
            logging.error('Error in market_summary_all', str(e))
            return JsonResponse({"error": str(e)}, status=500)
    else:
        logging.error('Method Not Allowed')
        return JsonResponse({"message": "Method Not Allowed"}, status=405)


def market_summary_for(request):
    '''
    Get Summary of a specific market
    request: GET
    params: market (str)
    '''
    if request.method == 'GET':
        try:
            logging.info('Request received for market_summary_for')
            api_key = request.META.get('HTTP_API_KEY')
            if api_key != CLIENT_KEY:
                return JsonResponse({"message": "Unauthorized Request"}, status=401)
            market = request.GET.get('market')
            url = f'{BITTREX_URL}markets/{market}/summary'
            headers = {'Accept': 'application/json', 'Apikey': BITTREX_KEY}
            response = requests.get(url, headers=headers)
            logging.info(f'Request completed for market_summary_for for market {market} => {response.json()}', )
            return JsonResponse(response.json(), status=200, safe=False)
        except Exception as e:
            logging.error(f'Error in market_summary_for for market {market}', str(e))
            return JsonResponse({"error": str(e)}, status=500)
    else:
        logging.error('Method Not Allowed')
        return JsonResponse({"message": "Method Not Allowed"}, status=405)

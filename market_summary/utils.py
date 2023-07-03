"""
This file contains the utility functions for the market_summary app.
"""
import logging
from django.http import JsonResponse
from config.common_config import CLIENT_KEY, COMMON_RESPONSE


def authenicate_token(view_func):
    """
    Decorator for authenticating the token.
    """
    def wrapper(request, *args, **kwargs):
        try:
            logging.info("Authenticating Request")
            api_key = request.META.get('HTTP_API_KEY')
            if api_key == CLIENT_KEY:
                return view_func(request, *args, **kwargs)
            else:
                return JsonResponse({"message": "Unauthorized Request"}, status=401)
        except Exception as exe:
            logging.error('Error While Authenticating Token: %s', exe)
            return JsonResponse(COMMON_RESPONSE['500'], status=500)
    return wrapper

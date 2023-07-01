from django.http import JsonResponse
from config.common_config import CLIENT_KEY
import logging


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
        except Exception as e:
            logging.error('Error in market_summary_all', str(e))
            return JsonResponse({"error": str(e)}, status=500)
    return wrapper

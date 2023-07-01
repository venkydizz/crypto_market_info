# Place to store configuration information for the application
import os

BITTREX_URL = 'https://api.bittrex.com/v3/'
ENDPOINTS = {
    'market_summary': f"{BITTREX_URL}markets/summaries",
    'market_summary_all': f"{BITTREX_URL}markets/<market>/summary",
}
# make sure to set the environment variables in the system
CLIENT_KEY = os.environ.get('CLIENT_KEY')

COMMON_RESPONSE = {
    '405': {"message": "Method Not Allowed"},
    '500': {"message": "Internal Server Error"},
    '401': {"message": "Unauthorized Request"},
}


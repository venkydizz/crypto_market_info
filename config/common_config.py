# Place to store configuration information for the application

BITTREX_URL = 'https://api.bittrex.com/v3/'
ENDPOINTS = {
    'market_summary': f"{BITTREX_URL}markets/summaries",
    'market_summary_all': f"{BITTREX_URL}markets/<market>/summary",
}
CLIENT_KEY = 'ab40713d69'

COMMON_RESPONSE = {
    '405': {"message": "Method Not Allowed"},
    '500': {"message": "Internal Server Error"},
    '401': {"message": "Unauthorized Request"},
}


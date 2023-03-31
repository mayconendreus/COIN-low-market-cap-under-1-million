import requests
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD',
    'sort': 'market_cap',
    'sort_dir': 'asc'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'f8cd6925-5a57-4d67-b8bf-e1bcdb11a47f',
}

market_cap_threshold = 1000000 # Maximum market cap threshold in USD

try:
    response = requests.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    
    # Get the coins with market cap lower than threshold
    target_coins = []
    for d in data['data']:
        if float(d['quote']['USD']['market_cap']) <= market_cap_threshold:
            target_coins.append(d['symbol'])
    
    # Print the target coins
    print('Target coins:')
    for coin in target_coins:
        print(coin)
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.TooManyRedirects) as e:
    print(e)


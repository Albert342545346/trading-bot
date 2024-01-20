from database import *
import requests



APIKEY = 'THimd3l6HiLDEikzgzRTBVaR5uSuVpBR'

COMPANY = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Google': 'GOOGL',
    'Facebook': 'FB',
    'Tesla': 'TSLA',
    'Intel': 'INTC',
    'NVIDIA': 'NVDA',
    'Coca-Cola': 'KO',
    'Walmart Inc.': 'WMT'
}



# Функция для получения данных о текущем положении акции
def get_stock_data(api_key, symbol):
    base_url = 'https://www.alphavantage.co/query'
    function = 'GLOBAL_QUOTE'
    api_url = f'{base_url}?function={function}&symbol={symbol}&apikey={api_key}'

    try:
        response = requests.get(api_url)
        data = response.json()

        if 'Global Quote' in data:
            global_quote = data['Global Quote']
            return global_quote
        else:
            print(f"Error: {data['Error Message']}")
            return None

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def getDataFromServer(name):
    stock_data = get_stock_data(APIKEY, COMPANY[name])

    if stock_data:
        symbol = stock_data['01. symbol']
        price = float(stock_data['05. price'])
        volume = int(stock_data['06. volume'])
        latest_time = stock_data['07. latest trading day']

        return {
                "name": symbol,
                "price": price,
                "volume": volume,
                "day": latest_time
                }
    return {}

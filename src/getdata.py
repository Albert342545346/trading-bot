import requests

def get_stock_data(symbol):
    api_key = 'THimd3l6HiLDEikzgzRTBVaR5uSuVpBR'
    base_url = 'https://www.alphavantage.co/query'
    
    # Формируем параметры запроса
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',  # Интервал запроса (может быть изменен)
        'apikey': api_key
    }
    
    try:
        # Отправляем запрос к API
        response = requests.get(base_url, params=params)
        data = response.json()
        
        # Печатаем результат (в данном случае, временные ряды за последний день)
        print(data)
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Пример использования функции для получения данных о акции Apple (AAPL)
get_stock_data('AAPL')

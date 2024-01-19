import requests

def get_trading_data(api_url, api_key):
    try:
        # Устанавливаем заголовок с ключом API
        headers = {
            'apikey': api_key
            # Замените 'Bearer' на необходимый тип авторизации, если это отличается
        }

        # Выполняем GET-запрос к API площадки с заголовками
        response = requests.get(api_url, headers=headers)

        # Проверяем успешность запроса (код 200 означает успешный запрос)
        if response.status_code == 200:
            # Возвращаем JSON-данные
            return response.json()
        else:
            # Если запрос не успешен, выводим сообщение об ошибке
            print(f"Ошибка запроса: {response.status_code}")
            return None

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None

# Пример использования: замените 'YOUR_API_URL' и 'YOUR_API_KEY' на реальные значения
api_url = 'https://www.alphavantage.co/query'
api_key = 'THimd3l6HiLDEikzgzRTBVaR5uSuVpBR'
trading_data = get_trading_data(api_url, api_key)

# Выводим полученные данные (если запрос был успешен)
if trading_data:
    print(trading_data)

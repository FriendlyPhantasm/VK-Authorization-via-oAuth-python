import requests
import webbrowser
import time

#параметры запроса на авторизацию
params = {
    'display': 'page',
    'client_id': '7780842',
    'redirect_uri': 'http://127.0.0.1:8080/',
    'response_type': 'code',
    'v': '5.130',
    'scope': 'docs,offline',
}

#получаем ссылку для авторизации
r = requests.get('https://oauth.vk.com/authorize', params=params)

#открываем ссылку в браузере
webbrowser.open(f'{r.url}')

#задержка для получения токена
time.sleep(5)

#получаем код авторзации с сервера
response = requests.get('http://127.0.0.1:8080/code').json()
params = {
    'redirect_uri': 'http://127.0.0.1:8080/',
    'client_id': '7780842',
    'client_secret': 'YymRx939ar0nVAQ2ohse',
    'code': response['code'],
}

#получаем access token пользователя для дальнейших запросов
response = requests.get(
    'https://oauth.vk.com/access_token', params=params).json()

#параметры запроса двух файлов пользователя с id 175906063 текстового типа
params = {
    "count": '2',
    "type": '1',
    "owner_id": '175906063',
    'access_token': response['access_token'],
    'v': '5.130',
}

r = requests.get(
    'https://api.vk.com/method/docs.get', params=params).json()
print(r)

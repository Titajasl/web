# На сайте портала открытых данных Москвы есть таблица 
# с популярными именами новорожденных. Напишите функцию, которая получает данные 
# при помощи requests и читает содержимое в формате json. 
# Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows

import requests

def get_data(url):
    result = requests.get(url)
    return result.json()

if __name__ == '__main__':
    data = get_data('http://api.data.mos.ru/v1/datasets/2009/rows')
    print(data)
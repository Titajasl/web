import requests

def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Что-то не так.')

if __name__ == '__main__':
    data = get_weather('http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=714158196fd77aeceb9d305c10ef097c&units=metric')
    print(data)    
from flask import Flask, abort, request
from req import get_weather
from datetime import datetime
from news_list import all_news
from get_data import get_data

city_id = 524901
apikey = '714158196fd77aeceb9d305c10ef097c'

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric' % (city_id, apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    result = '<p><b>Температура:</b> %s\n<p>' % weather['main']['temp']
    result += '<p><b>Город:</b> %s<p>' % weather ['name']
    result += '<p><b>Дата:</b> %s</p>' % cur_date
    return result

@app.route('/news')
def all_the_news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit)

@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>'
        result = result % news_to_show[0]
        return result
    else:
        abort(404)

# 1. Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных,
#    получаемые при помощи функции из предыдущей задачи.
# 2. Ограничьте выводимые данные одним годом. 
#    Год должен указываться в URL как параметр, например /names?year=2016.
@app.route('/names')
def names():
    data = get_data('http://api.data.mos.ru/v1/datasets/2009/rows')     # получаем список данных по ссылке
    try:                                        # получаем year
        year = int(request.args.get('year'))
    except:
        year = None

        # заголовки колонок таблицы
    name_table = '''                    
            <table>
                <tr>
                    <th>Год</th>
                    <th>Месяц</th>
                    <th>Имя</th>
                    <th>Кол-во</th>
                </tr>
            </table>
            '''
        # данные таблицы
    if year:                                    # eсли есть year
        for note in data:           
            if year == note['Cells']['Year']:
                name_table += '''
                    <table>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                        </tr>
                    </table>
                    ''' % (note['Cells']['Year'], note['Cells']['Month'], note['Cells']['Name'], note['Cells']['NumberOfPersons'])
    else:                                       # если нет year
        for note in data:
            name_table += '''
                <table>
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>
                </table>
                ''' % (note['Cells']['Year'], note['Cells']['Month'], note['Cells']['Name'], note['Cells']['NumberOfPersons'])

    return name_table

if __name__ == '__main__':
    app.run()
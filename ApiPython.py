import json
import requests
main_api = 'http://api.openweathermap.org/data/2.5/weather?q='
key = ':)'

def apiLookUp():
    address = input('city name: ')
    end_plus = main_api+address+'&appid='+key+"&units=metric"
    json_data = requests.get(end_plus).json()
    try:
        x = json_data['main']
        y = x['temp']
        print(y)
        apiLookUp()
    except:
        print('city not found')
        apiLookUp()

apiLookUp()

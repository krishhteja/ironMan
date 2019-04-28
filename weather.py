import json
import requests

def current(location):
    url = "https://community-open-weather-map.p.rapidapi.com/weather?id=2172797&units=metric&mode=JSON&q="+location
    response = requests.get(url,
      headers={
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
        "X-RapidAPI-Key": "USE KEY HERE "
      }
    )
    data = json.loads(response.text)
    map = {}
    map['temp'] = str(data['main']['temp'])
#    map['pressure'] = data['main']['pressure']
    map['humidity'] = str(data['main']['humidity'])
    map['minimumTemp'] = str(data['main']['temp_min'])
    map['maximumTemp'] = str(data['main']['temp_max'])
    map['description'] = str(data['weather'][0]['description'])
    return map

def forecast(location):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast?q="+location
    response = requests.get(url,
        headers={
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
            "X-RapidAPI-Key": "USE KEY HERE "
        }
    )
    data = json.loads(response.text)
    responseMap = {}
    for element in data['list']:
        map = {}
        date = element['dt_txt']
        map['temp'] = str(element['main']['temp'])
        map['humidity'] = str(element['main']['humidity'])
        map['minimumTemp'] = str(element['main']['temp_min'])
        map['maximumTemp'] = str(element['main']['temp_max'])
        map['description'] = str(element['weather'][0]['description'])
        responseMap[date] = map
    return responseMap

if __name__ == '__main__':
    print("hello! Logs In weather")
    current = forecast('Lappeenranta')
    printArr = []

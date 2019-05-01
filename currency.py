import json
import requests

def convert(fromCurrency, to):
    fromCode = list(fromCurrency)
    toCode = list(to)
    if 'found' in fromCode or 'found' in toCode:
        map = {}
        map['status'] = 'failed'
    else:
        check = fromCode.split('#')[0]+"_"+toCode.split('#')[0]
        url = "https://free.currconv.com/api/v7/convert?q="+check+"&compact=ultra&apiKey=a5504e19bdf18346c7dc"
        response = requests.get(url)
        data = json.loads(response.text)
        map = {}
        map['status'] = 'success'
        map['fromCurrency'] = fromCode.split('#')[1]
        map['toCurrency'] = toCode.split("#")[1]
        map['exchange'] = data[check]
    return map

def list(countryName):
    url = "https://free.currconv.com/api/v7/currencies?apiKey=a5504e19bdf18346c7dc"
    response = requests.get(url)
    data = json.loads(response.text)
    countries = data['results']
    for country in countries:
        currency = countries[country]['currencyName']
        if countryName.lower() in currency.lower():
            return country+"#"+countries[country]['currencyName']
    return "country not found"

#a5504e19bdf18346c7dc
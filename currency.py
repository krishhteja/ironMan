import json
import requests

def convert(fromCurrency, to):
    fromCode = list(fromCurrency)
    toCode = list(to)
    print(fromCode + " -- " + toCode)
    check = fromCode.split('#')[0]+"_"+toCode.split('#')[0]
    url = "https://free.currconv.com/api/v7/convert?q="+check+"&compact=ultra&apiKey=a5504e19bdf18346c7dc"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    map = {}
    map['fromCurrency'] = fromCode.split('#')[1]
    map['toCurrency'] = toCode.split("#")[1]
    map['exchange'] = data[check]
    return map

def list(countryName):
    print(countryName)
    url = "https://free.currconv.com/api/v7/currencies?apiKey=a5504e19bdf18346c7dc"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    countries = data['results']
    for country in countries:
        currency = countries[country]['currencyName']
        #print(countryName.lower() + " -- " + currency.lower())
        if countryName.lower() in currency.lower():
            return country+"#"+countries[country]['currencyName']
    return "country not found"

#a5504e19bdf18346c7dc
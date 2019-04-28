import json
import requests

def movieInfo(name):
    url = "http://www.omdbapi.com/?apikey=71fc0148&t="+name+"&plot=full"
    response = requests.get(url)
    data = json.loads(response.text)
    map = {}
    if 'Title' in data:
        map['response'] = 'success'
        map['title'] = data['Title']
        map['year'] = data['Year']
        map['rating'] = data['Rated']
        map['release'] = data['Released']
        map['runTime'] = data['Runtime']
        map['genre'] = data['Genre']
        map['director'] = data['Director']
        map['actors'] = data['Actors']
        map['plot'] = data['Plot']
        map['language'] = data['Language']
        map['imdbrating'] = data['imdbRating']
        map['votes'] = data['imdbVotes']
        map['production'] = data['Production']
    else:
        map['response'] = 'No movie found'
    return map

if __name__ == '__main__':
    print("hello! Logs In movies")
import os
import speech_recognition as speechRec
import pyttsx3
import itunes as itunes
import google as google
import geocoder
import weather as weather
import pandas as pd
import movie as movie
import currency as currency
import sports as sports
import translate as translate
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

'''bot = ChatBot('Charlie')
trainer = ListTrainer(bot)

for files in os.listdir('/Users/krishnavaddepalli/PycharmProjects/IronMan/chatterbot-corpus-master/chatterbot_corpus/data/english'):
    data = open('/Users/krishnavaddepalli/PycharmProjects/IronMan/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files, 'r').readlines()
    trainer.train(data)
'''
speech = speechRec.Recognizer()
try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested Driver not found")
except RuntimeError:
    print("pyttsx3 Driver init failed")

voices = engine.getProperty("voices")

#for voice in voices:
#    print(voice.id)
#    print(voice.languages)
#    print(" - " + voice.gender)

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

def readCommand(cmd):
    engine.say(cmd)
    engine.runAndWait()

def listenCommand():
    voiceText = ''
    print("Listening for user command")
    with speechRec.Microphone() as source:
        userSpeech = speech.listen(source)
        print(userSpeech)

    try:
        voiceText = speech.recognize_google(userSpeech)
    except speechRec.UnknownValueError:
        readCommand("Value not found")
        print("Value not found")
    except speechRec.RequestError as reqErr:
        readCommand("Error with network")
        print("Network error")
    return voiceText

if __name__ == '__main__':
    readCommand("Hello Boss! Voice command activated.")

    while True:
        userMode = listenCommand()
        print('cmd : ' + format(userMode))
        if 'hello' in userMode.lower():
            readCommand("Hey Boss!")
            continue
        elif 'how are you' in userMode.lower():
            readCommand("Great ... as always!")
            continue
        elif 'open' in userMode.lower():
            itunes.open()
            continue
        elif 'play' in userMode.lower():
            itunes.play()
            continue
        elif 'pause' in userMode.lower():
            itunes.pause()
            continue
        elif 'next' in userMode.lower():
            itunes.nextSong()
            continue
        elif 'previous' in userMode.lower():
            itunes.previousSong()
            continue
        elif 'increase' in userMode.lower():
            itunes.volumeUp()
            continue
        elif 'decrease' in userMode.lower():
            itunes.volumeDown()
            continue
        elif 'movie' in userMode.lower():
            movieName = format(userMode).split('movie')[1]
            info = movie.movieInfo(movieName)
            if info['response'] == 'success':
                readCommand("Name of the movie is " + info['title'] + ". It is released on " + info['release'] + " with a run time of " + info['runTime'] + ". It is released in " + info['language'] + ". It's a " + info['genre'] + " movie produced by " + info['production'] + ", directed by " + info['director'] + ", and played by " + info['actors'] + ". The main plot is " + info['plot'])
                if info['rating'] == 'N/A':
                    readCommand("It's rating is not provided")
                else:
                    readCommand("It has a rating of " + info['imdbrating'] + " rated by " + info['votes'] + " people")
        elif 'google' in userMode.lower():
            movieName = format(userMode).lower().split('google')[1]
            google.open(movieName)
        elif 'weather' in userMode.lower():
            location = geocoder.ip('me')
            current = weather.current(location.city)
            readCommand(
                "Currently it's " + current['temp'] + " degrees in " + location.city + ". Today's minimum stands at " +
                current['minimumTemp'] + " degrees and maximum is " + current['maximumTemp'] + " with a humidity of " +
                current['humidity'] + " and " + current['description'])
            continue
        if 'convert' in userMode.lower():
            splitData = format(userMode).split('convert')[1]
            fromCurrency = splitData.split('to')[0]
            toCurrency = splitData.split('to')[1]
            conversion = currency.convert(fromCurrency.strip(), toCurrency.strip())
            if conversion['status'] == 'success':
                readCommand("Converting {} to {} is currently at {}".format(str(conversion['fromCurrency']), str(conversion['toCurrency']), str(conversion['exchange'])))
            else:
                readCommand("Currency not found!")
        if 'translate' in userMode.lower():
            splitData = format(userMode).split('translate')[1]
            word = splitData.split('to')[0]
            toLanguage = splitData.split('to')[1].strip()
            print(word, toLanguage.strip())
            tarjuma = translate.translation(word, toLanguage.strip())
            readCommand(tarjuma)
        elif 'perfect' in userMode.lower():
            readCommand("As always!")
            continue
        elif 'cricket' in userMode.lower():
            scores = sports.cricketMatches()
            if len(scores) > 0:
                for score in scores:
                    readCommand("Match between " + score['between'] + " is happening at " + score['location'] + ". As part of series " + score['series'] + ". The current status is " + score['status'] + " and " + score['score'])
            else:
                readCommand("Currently I see no live matches being played")
            continue
        elif 'football' in userMode.lower():
            scores = sports.currentFootballMatches()
            if scores['status'] == 'true':
                readCommand("The current match is between " + scores['between'] + ". " + scores['scores'])
                if scores['homeScores'] != '':
                    readCommand(scores['homeScorers'])
                if scores['awayScorers'] != '':
                    readCommand(scores['awayScorers'])
                readCommand("Statistics of the match are " + scores['statistics'])
            else:
                readCommand("Currently I see no live matches being played")
        elif 'forecast' in userMode.lower():
            location = geocoder.ip('me')
            current = weather.forecast(location.city)
            readCommand("It's hard to explain the forecast. I'm drawing it up on the display.")
            printArr = []
            for individual in current:
                temporaryArr = []
                temporaryArr.append(individual)
                temporaryArr.append(current[individual]['temp'])
                temporaryArr.append(current[individual]['minimumTemp'])
                temporaryArr.append(current[individual]['maximumTemp'])
                temporaryArr.append(current[individual]['description'])
                printArr.append(temporaryArr)
            print(pd.DataFrame(printArr, columns=['Time', 'Temperature', 'Minimum Temperature', 'Maximum Temperature', 'Description']))
            continue

        elif 'bye' in userMode.lower():
            readCommand("Bye Boss!")
            exit()
#        else:
#            print("abc")
            #bot.get_response(userMode)
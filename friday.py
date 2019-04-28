import speech_recognition as speechRec
import pyttsx3
import itunes as itunes
import google as google
import geocoder
import weather as weather
import pandas as pd

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
    readCommand("Hello Krishna. How are you doing?")

    while True:
        userMode = listenCommand()
        print('cmd : ' + format(userMode))
        if 'hello' in userMode:
            readCommand("Hey love!")
            continue
        elif 'open' in userMode:
            itunes.open()
            continue
        elif 'play' in userMode:
            itunes.play()
            continue
        elif 'pause' in userMode:
            itunes.pause()
            continue
        elif 'next' in userMode:
            itunes.nextSong()
            continue
        elif 'previous' in userMode:
            itunes.previousSong()
            continue
        elif 'increase' in userMode:
            itunes.volumeUp()
            continue
        elif 'decrease' in userMode:
            itunes.volumeDown()
            continue
        elif 'Google' in userMode:
            google.open(format(userMode.replace('Google ', '')))
        elif 'weather' in userMode:
            location = geocoder.ip('me')
            current = weather.current(location.city)
            readCommand(
                "Currently it's " + current['temp'] + " degrees in " + location.city + ". Today's minimum stands at " +
                current['minimumTemp'] + " degrees and maximum is " + current['maximumTemp'] + " with a humidity of " +
                current['humidity'] + " and " + current['description'])
            continue
        elif 'forecast' in userMode:
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

        elif 'bye' in userMode:
            readCommand("Bye Krishna. Will miss you love.")
            exit()
import subprocess
import os

'''Gets info of current song'''
def info():
    global state
    state = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to player state as string'")
    global artist
    artist = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to artist of current track as string'")
    global track
    track = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to name of current track as string'")
    global currentvolume
    currentvolume = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'")

'''Open iTunes'''
def open():
    print("iTunes currently closed. Opening iTunes")
    os.system("open -a iTunes")
    print("iTunes running")

'''Current status of itunes'''
def status():
    info()
    if (state == "playing"):
        print("Itunes is: %s" % state)
        print("Currently playing: '%s' by '%s'" % (track, artist))
    else:
        print("Itunes it not playing, type 'itunes play' to start playing music")

'''Play current song'''
def play():
    state = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to player state as string'")
    print(state)
    if(state == "stopped"):
        open()
        subprocess.getoutput("osascript -e 'tell application \"iTunes\" to play'")
        info()
        print("Currently playing: '%s' by '%s'" % (track, artist))
    elif (state == "paused"):
        info()
        print("current status is paused.")
        subprocess.getoutput("osascript -e 'tell application \"iTunes\" to play'")
        print("Currently playing: '%s' by '%s'" % (track, artist))
    else:
        print("Itunes is currently playing")

'''Pause the song'''
def pause():
    info()
    if (state == "playing"):
        print("Pausing iTunes")
        subprocess.getoutput("osascript -e 'tell application \"iTunes\" to pause'")
        print("iTunes paused")
    else:
        print("iTunes is currently paused")

'''Continue to next song'''
def nextSong():
    print("Continuing to next song")
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to next track'")
    print("Currently playing: '%s' by '%s'" % (track, artist))


def previousSong():
    print("Rewinding to previous song")
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to previous track'")
    status()

def quitiTunes():
    print("Quitting iTunes")
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to quit'")


def mute():
    print("Muting iTunes")
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set mute to true'")


def unMute():
    print("Unmuting iTunes")
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set mute to false'")


def volumeUp():
    info()
    increaseby = 10
    if (currentvolume > "90"):
        increaseby = 100 - int(currentvolume)
    elif (currentvolume < "90"):
        increaseby = 10;
    newvolume = int(currentvolume) + increaseby
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set sound volume to " + str(newvolume) + "'")
    print("Volume increased by 10")


def volumeDown():
    info()
    decreaseby = 10
    if (currentvolume < "10"):
        decreaseby = int(currentvolume)
    elif (currentvolume > "10"):
        decreaseby = 10
    newvolume = int(currentvolume) - decreaseby
    subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set sound volume to " + str(newvolume) + "'")
    print("Volume Reduced by 10")

if __name__ == '__main__':
    print("hello! In itunes")
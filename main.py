import ctypes
import os
import keyboard
import time
import webbrowser

#caloocan location
path = os.getcwd()

#Lyrics ni boi
lyrics = """Eh, paano kung hindi
Hindi ka nakilala?
Siguro, nakakulong pa di
Sa nakaraan, 'di makalaya\n"""

def caloocan_music():
    webbrowser.open('https://www.youtube.com/watch?v=0yz8l25jZgA')

def caloocan_lyrics():
    #susig na notepad
    os.startfile('notepad')
    #matulog kasi pagod
    time.sleep(0.5)
    #type /w delay each letter
    keyboard.write(lyrics,0.1)

def caloocan_bg_img():
    #change walpapir
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\caloocanBoi.png", 0)


if __name__ == '__main__':
    #Run
    caloocan_music()
    keyboard.press("windows")
    keyboard.press("d")
    keyboard.release("windows")
    caloocan_bg_img()
    caloocan_lyrics()
    #gi tapolan kog himo sa exit :) e off ra ninyos task manager goodluck <3



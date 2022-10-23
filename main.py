import ctypes
import os
import keyboard
import time
import webbrowser

#current directory path
path = os.getcwd()

#Lyrics
lyrics = """Eh, paano kung hindi
Hindi ka nakilala?
Siguro, nakakulong pa di
Sa nakaraan, 'di makalaya\n"""

#Opens deafult browser and plays directed link to->
def caloocan_music():
    webbrowser.open('https://www.youtube.com/watch?v=fV8lnDKTl4M')

def caloocan_lyrics():
    #Opens Notepad
    os.startfile('notepad')
    #Waits half a sec
    time.sleep(0.5)
    #types lyrics to notepad with 0.1 sec delay
    keyboard.write(lyrics,0.1)

def caloocan_bg_img():
    #cahnges host wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\caloocanBoi.png", 0)


if __name__ == '__main__':
    #Run
    caloocan_music()
    time.sleep(1)
    keyboard.press("windows")
    keyboard.press("d")
    keyboard.release("windows")
    caloocan_bg_img()
    caloocan_lyrics()
    #gi tapolan kog himo sa exit :) e off ra ninyos task manager goodluck <3



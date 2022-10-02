import ctypes
import os
import keyboard
import time

#caloocan location
path = os.getcwd()

#Lyrics ni boi
lyrics = """Eh, paano kung hindi
Hindi ka nakilala?
Siguro, nakakulong pa di
Sa nakaraan, 'di makalaya\n

Ang sarili, dinadaya
Yeah, naglalasing-lasing, hindi pala kaya    
Yeah, ayokong magising nang 'di ka kasama
Kung nandito ka sa tabi, mas masaya sana\n

Ngayon, hinahanap ka, nasasaktan
Buti na lang, may alak pa na nasasandalan
Dinadaan ko lang sa amat ang nararamdaman
Para naman kahit papa'no gumaan\n
"""



def caloocan_lyrics():
    #susig na notepad
    os.startfile('notepad')
    #matulog kasi pagod
    time.sleep(0.5)
    #type /w delay each letter
    keyboard.write(lyrics,0.2)

def caloocan_bg_img():
    #change walpapir
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\caloocanBoi.png", 0)


if __name__ == '__main__':
    #Run
    caloocan_bg_img()
    caloocan_lyrics()
    #gi tapolan kog himo sa exit :) e off ra ninyos task manager goodluck <3



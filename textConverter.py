from gtts import gTTS
import os
from tkinter import *

def TextConvertor(entry1):
    lang = 'en'
    GTTS = gTTS(text=entry1.get(), lang = lang, slow=False)
    GTTS.save('speech.mp3')

    os.system("mpg321 speech.mp3")


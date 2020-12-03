import speech_recognition as sr 
from tkinter import *

r = sr.Recognizer()

def Convert(label1):
    with sr.Microphone() as s2:
        label1.config(text="Talk .... ")
        r.adjust_for_ambient_noise(s2,duration=0.2)

        audio2 = r.listen(s2)
        try:
            label1.config(text = f"Text: {r.recognize_google(audio2)}")
        except:
            label1.config(text = f"Sorry, I did not get that")
import speech_recognition as sr
from gtts import gTTS
import os
import time
import pyaudio
import playsound


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


#speak("Hello")
#get_audio()
text = get_audio()

if "Hi" in text:
    speak("How, are you?")
elif "What is your name?" in text:
    speak("My Name ist lionel")

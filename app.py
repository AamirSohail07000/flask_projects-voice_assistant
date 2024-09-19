from flask import Flask
import speech_recognition as sr
import webbrowser
import pyttsx3

app = Flask(__name__)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

@app.route('/')

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello Aamir How may I help you ?")
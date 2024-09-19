from flask import Flask
import speech_recognition as sr
import webbrowser
import pyttsx3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import os

app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle voice command
@app.route('/process_voice', methods=['POST'])
def process_voice():
    data = request.get_json()
    command = data.get('command')
    
    if command:
        processCommand(command)  # Process the command
        return jsonify({"status": "success", "command": command})
    return jsonify({"status": "error", "message": "No command received"})


def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    else:
        speak("Sorry, I did not understand the command.")

# Function to give voice response using pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    app.run(debug=True)

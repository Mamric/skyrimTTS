import speech_recognition
import pyttsx3
import playsound
from gtts import gTTS

import random
import pathlib
import os

def bot_speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()
    print(audio_string)

def get_audio_from_mic(mic):
    recognizer.adjust_for_ambient_noise(mic)
    audio = recognizer.listen(mic)
    text = recognizer.recognize_google(audio)
    text = text.lower()
    return text


if __name__ == "__main__":
    engine = pyttsx3.init()
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                text = get_audio_from_mic(mic)

                bot_speak(f"Recognized {text}")
        except speech_recognition.UnknownValueError:
        # except:
            recognizer = speech_recognition.Recognizer()
            continue
import speech_recognition
import pyttsx3


def bot_speak(audio_string):
    '''Takes in a string and says it with tts, then logs with print'''
    engine.say(audio_string)
    engine.runAndWait()
    print(audio_string)

def get_audio_from_mic(mic):
    '''Takes in a speechrecognition mic and listens for audio'''
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
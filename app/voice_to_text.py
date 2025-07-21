import os
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio_if_needed(input_data):
    if isinstance(input_data, str) and input_data.endswith(".wav") and os.path.exists(input_data):
        recognizer = sr.Recognizer()
        audio = AudioSegment.from_wav(input_data)
        audio.export("converted.wav", format="wav")
        with sr.AudioFile("converted.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                return "Sorry, could not understand the audio."
    return input_data

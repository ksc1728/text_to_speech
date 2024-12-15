
!pip install gtts

!pip install --upgrade pip

!pip install SpeechRecognition

!apt-get update
!apt-get install portaudio19-dev python3-dev
!pip install PyAudio

from gtts import gTTS
import os
import speech_recognition as sr

def text_to_speech():
    text=input()
    tts = gTTS(text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    os.system(f"start {filename}")

text_to_speech()
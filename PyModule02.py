import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr
import os

fs = 44100
seconds = 5

print("Speak Command...")

audio = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1,
    dtype=np.int16
)

sd.wait()

write("recording.wav", fs, audio)

r = sr.Recognizer()

with sr.AudioFile("recording.wav") as source:
    audio_data = r.record(source)

try:
    command = r.recognize_google(audio_data)

    print("You said:", command)

    command = command.lower()

    if "open calculator" in command:
        os.system("calc")

    elif "open notepad" in command:
        os.system("notepad")

    elif "open chrome" in command:
        os.system(
            r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
        )

    else:
        print("Command not recognized")

except Exception as e:
    print("Error:", e)
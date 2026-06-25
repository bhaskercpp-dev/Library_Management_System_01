import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr
import subprocess

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

    command = command.lower().strip()

    if "calculator" in command:
        print("Opening Calculator")
        subprocess.Popen(["calc"])

    elif "notepad" in command:
        print("Opening Notepad")
        subprocess.Popen(["notepad"])

    elif "chrome" in command:
        print("Opening Chrome")
        subprocess.Popen([
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        ])

    else:
        print("Command not recognized")

except Exception as e:
    print("Error:", e)
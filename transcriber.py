import speech_recognition as sr
import os

# Path to the audio files folder
folder_path = "audio_files"

# Get the list of audio files in the folder
audio_files = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".wav"):
        file_path = os.path.join(folder_path, file_name)
        audio_files.append(file_path)

print(audio_files)

# Create a recognizer object and load the audio file
recognizer = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Perform speech recognition on the audio
text = recognizer.recognize_google(audio_data)
print("Transcription: " + text)

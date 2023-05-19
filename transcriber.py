import speech_recognition as sr

audio_file = "audio_files/untitled.wav"

# Create a recognizer object and load the audio file
recognizer = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Perform speech recognition on the audio
text = recognizer.recognize_google(audio_data)
print("Transcription: " + text)

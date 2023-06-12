import speech_recognition as sr
import os


class Transcriber:

    def __init__(self):
        self.audio_files = None
        self.folder_path = None

    def get_audio_files(self):
        self.audio_files = []
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".wav"):
                file_path = os.path.join(self.folder_path, file_name)
                self.audio_files.append(file_path)

    # return a list of dicts. dicts have "file_name" and "text" keys.
    def transcribe_files(self):
        recognizer = sr.Recognizer()
        all_transcriptions = []
        for audio_file in self.audio_files:
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                print(audio_data)
                # Perform speech recognition on the audio
                transcription = {"file_name": audio_file, "text": recognizer.recognize_whisper(audio_data)}
                all_transcriptions.append(transcription)
        return all_transcriptions

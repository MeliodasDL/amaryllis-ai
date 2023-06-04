# communication_preferences.py
import os
import json
import pyaudio
import speech_recognition
import googletrans
import pyttsx3


class CommunicationPreferences:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = self.load_preferences()

    def load_preferences(self):
        # Load user preferences from a file or database
        # Example: preferences = {"language": "en", "accent": "us", "gender": "female", "notifications": True}
        preferences = {}
        try:
            with open(f"user_preferences_{self.user_id}.json", "r") as file:
                preferences = json.load(file)
        except FileNotFoundError:
            # Set default preferences if no file is found
            preferences = {
                "language": "en",
                "accent": "us",
                "gender": "female",
                "notifications": True,
            }
            self.save_preferences(preferences)
        return preferences

    def save_preferences(self, preferences):
        # Save user preferences to a file or database
        with open(f"user_preferences_{self.user_id}.json", "w") as file:
            json.dump(preferences, file)

    def set_language(self, language):
        self.preferences["language"] = language
        self.save_preferences(self.preferences)

    def set_accent(self, accent):
        self.preferences["accent"] = accent
        self.save_preferences(self.preferences)

    def set_gender(self, gender):
        self.preferences["gender"] = gender
        self.save_preferences(self.preferences)

    def set_notifications(self, notifications):
        self.preferences["notifications"] = notifications
        self.save_preferences(self.preferences)

    def text_to_speech(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if selected_voice := next(
            (
                voice
                for voice in voices
                if (
                    voice.languages[0].startswith(self.preferences["language"])
                    and voice.gender.lower() == self.preferences["gender"]
                    and voice.id.lower().find(self.preferences["accent"]) != -1
                )
            ),
            None,
        ):
            engine.setProperty("voice", selected_voice.id)
        else:
            # Fallback to default voice if no matching voice is found
            engine.setProperty("voice", voices[0].id)
        engine.say(text)
        engine.runAndWait()

    def speech_to_text(self):
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        with microphone as source:
            print("Please speak...")
            audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(
                audio, language=self.preferences["language"]
            )
        except speech_recognition.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except speech_recognition.RequestError:
            print("Sorry, there was an error processing your speech.")
            return None

    def translate_text(self, text, target_language):
        translator = googletrans.Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text

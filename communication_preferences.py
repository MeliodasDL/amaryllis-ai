# communication_preferences.py
import googletrans
import mysql.connector
import pyttsx3
import speech_recognition

from config import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD


class CommunicationPreferences:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = self.load_preferences()

    def load_preferences(self):
        # Load user preferences from the database
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME,
        )
        cursor = connection.cursor()
        cursor.execute("SELECT language, accent, gender, notifications FROM user_preferences WHERE user_id = %s", (self.user_id,))
        result = cursor.fetchone()

        if result:
            preferences = {
                "language": result[0],
                "accent": result[1],
                "gender": result[2],
                "notifications": result[3],
            }
        else:
            # Set default preferences if no record is found
            preferences = {
                "language": "en",
                "accent": "us",
                "gender": "female",
                "notifications": True,
            }
            self.save_preferences(preferences)

        connection.close()
        return preferences

    def save_preferences(self, preferences):
        # Save user preferences to the database
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME,
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO user_preferences (user_id, language, accent, gender, notifications) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE language = %s, accent = %s, gender = %s, notifications = %s",
            (
                self.user_id,
                preferences["language"],
                preferences["accent"],
                preferences["gender"],
                preferences["notifications"],
                preferences["language"],
                preferences["accent"],
                preferences["gender"],
                preferences["notifications"],
            ),
        )
        connection.commit()
        connection.close()

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

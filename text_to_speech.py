import pyttsx3

class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def welcome(self):
        self.speak("Welcome to Gesture2Visual.")

    def no_hand_detected(self):
        self.speak("No hand detected.")

    def gesture_detected(self, gesture):
        self.speak(f"Detected gesture: {gesture}")


def speak(text):
    tts = TextToSpeech()
    tts.speak(text)


if __name__ == "__main__":
    assistant = TextToSpeech()

    assistant.welcome()
    assistant.gesture_detected("Hello")

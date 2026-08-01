import random

class SignClassifier:

    def __init__(self):
        self.labels = [
            "Hello",
            "Thank You",
            "Yes",
            "No",
            "Help",
            "Please",
            "Stop",
            "Good Morning"
        ]

    def preprocess(self, landmarks):
        if len(landmarks) == 0:
            return None
        return landmarks

    def predict(self, landmarks):
        processed = self.preprocess(landmarks)

        if processed is None:
            return "No Hand Detected"

        # Placeholder prediction
        prediction = random.choice(self.labels)

        return prediction


if __name__ == "__main__":

    classifier = SignClassifier()

    print("Testing Gesture Prediction...")

    print(classifier.predict([[0.1, 0.2, 0.3]]))

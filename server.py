"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the emotion detector interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Analyze the submitted text and return emotion results."""
    text_to_analyze = request.values.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if not result:
        return "Emotion service is currently unavailable.", 503

    if result["dominant_emotion"] is None:
        return "Unable to analyze the supplied text.", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

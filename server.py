"""
Flask server for EmotionDetection Web Application.

This module defines the Flask app, loads the emotion_detector
function from the EmotionDetection package, and exposes the web
endpoints used by the client.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main HTML homepage.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Route to analyze emotional content of text.

    Returns a formatted sentence describing the emotion scores
    or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_string


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

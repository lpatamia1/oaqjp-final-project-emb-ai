"""
Flask app to analyze emotions using Watson NLP service.
"""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Route to process the user's input text and return emotion analysis.
    """
    text_to_analyze = request.form.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_output = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_output

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_dect():
    """
    Endpoint to detect emotions from the given text.

    Args:
        textToAnalyze (str): The text to analyze for emotion detection.

    Returns:
        str: Rendered HTML template displaying the detected emotions and the dominant emotion.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyse)
    dominant_emotion = max(emotions, key=emotions.get)
    
    if dominant_emotion:
        print(f"Dominant emotion detected is: {dominant_emotion}")
    else:
        print("Error, Please insert some text.")
        
    emotions_str = ', '.join([f"'{k}': {v}" for k, v in emotions.items()])
    return render_template('emotion_results.html', emotions_str=emotions_str, dominant_emotion=dominant_emotion)

@app.route('/')
def home():
    """
    Home endpoint to render the home page.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

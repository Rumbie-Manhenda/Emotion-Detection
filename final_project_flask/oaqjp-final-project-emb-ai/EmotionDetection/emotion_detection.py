import json
import requests
from typing import Dict, Optional

def emotion_detector(text_to_analyze: str) -> Optional[Dict[str, float]]:
    """
    Detects the emotions in the given text using the Watson NLP service.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        Optional[Dict[str, float]]: A dictionary containing the detected emotions and their scores,
        or None if an error occurred.
    """
    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        payload = {"raw_document": {"text": text_to_analyze}}

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        formatted_text = response.json()
        emotions = formatted_text['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        print(f"The dominant emotion is: {dominant_emotion}")
      

        emotions['dominant_emotion'] = max(emotions.values())
        return emotions

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error: Invalid response format. {e}")
    except Exception as e:
        print(f"Error: {e}")

    return None

if __name__ == '__main__':
    text = "I love myself"
    emotions = emotion_detector(text)
    if emotions:
        print(f"Emotions for {text}: {emotions}")
    else:
        print("Failed to detect emotions.")

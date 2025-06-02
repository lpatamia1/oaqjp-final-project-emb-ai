import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=data)

    # ✅ Handle blank input: return all None if status code is 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        parsed = response.json()
        if isinstance(parsed, str):
            parsed = json.loads(parsed)

        emotions = parsed['emotionPredictions'][0]['emotion']
        dominant = max(emotions, key=emotions.get)

        return {
            'anger': int(emotions['anger'] * 100),
            'disgust': int(emotions['disgust'] * 100),
            'fear': int(emotions['fear'] * 100),
            'joy': int(emotions['joy'] * 100),
            'sadness': int(emotions['sadness'] * 100),
            'dominant_emotion': dominant
        }

    except Exception:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

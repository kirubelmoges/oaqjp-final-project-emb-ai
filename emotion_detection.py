import requests
import json

def emotion_detector(text_to_analyse):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers=headers, json=input_json)

    return response.text


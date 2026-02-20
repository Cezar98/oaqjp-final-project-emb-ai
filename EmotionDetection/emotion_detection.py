import requests
import json 

def emotion_detector(text_to_analyze):
    response =  requests.post(url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', json={ "raw_document": { "text": text_to_analyze } }, headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"})
    response = response.json()['emotionPredictions'][0]['emotion']
    
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    res = {
        'anger':anger_score,
        'disgust':disgust_score,
        'fear':fear_score,
        'joy':joy_score,
        'sadness':sadness_score
    }
    res['dominant_emotion'] = max(res, key=res.get)
    return res
   

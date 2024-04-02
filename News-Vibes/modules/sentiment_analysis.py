from transformers import pipeline
from utils.constants import MODEL_NAME

def init_classifier():
    return pipeline("sentiment-analysis", model=MODEL_NAME)

def analyze_sentiment(classifier, text):
    result = classifier(text)[0]
    return result['label']

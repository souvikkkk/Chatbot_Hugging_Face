from transformers import pipeline

def load_model():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

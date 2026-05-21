import pickle
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

model = pickle.load(open("model.pkl", "rb"))
words, labels = pickle.load(open("data.pkl", "rb"))

with open("intents.json") as file:
    intents = json.load(file)

def predict_class(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens]

    bag = [1 if w in tokens else 0 for w in words]
    result = model.predict([bag])[0]

    return labels[result]

def get_response(sentence):
    tag = predict_class(sentence)

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

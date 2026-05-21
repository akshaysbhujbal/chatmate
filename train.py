import json
import pickle
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load dataset
with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
documents = []

# Preprocessing
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        documents.append((tokens, intent["tag"]))
    labels.append(intent["tag"])

words = [lemmatizer.lemmatize(w.lower()) for w in words]
words = sorted(set(words))
labels = sorted(set(labels))

# Training data
training = []
output = []

for doc in documents:
    bag = []
    pattern_words = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]

    for word in words:
        bag.append(1 if word in pattern_words else 0)

    training.append(bag)
    output.append(labels.index(doc[1]))

X = np.array(training)
y = np.array(output)

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and data
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump((words, labels), open("data.pkl", "wb"))

print("Training completed successfully.")

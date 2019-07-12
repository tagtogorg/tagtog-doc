################################################################################
#   Project: ML-tagtog
#   File: train_model.py
#   Authors:
#           (c) Uxio Garcia Andrade - uxiog21@gmail.com
#           (c) some random guys in the internet -- TODO find out who
##############################################################################

from keras.layers import SimpleRNN, Embedding, Dense, LSTM
from keras.models import Sequential

import pandas as pd
import numpy as np

from keras.layers import SimpleRNN, Embedding, Dense, LSTM
from keras.models import Sequential

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from keras.models import model_from_json

from numpy import loadtxt
from keras.models import load_model
from model_initialization import sentence_processing

def train_model(text,label,model,tokenizer):
    train_texts = []
    train_labels = []
    train_texts.append(text)

    #Process data the same way as in the model initialization
    if label == False:
        train_labels.append(0)
    else:
        train_labels.append(1)

    train_texts = np.asarray(train_texts)
    train_labels = np.asarray(train_labels)

    sequences = tokenizer.texts_to_sequences(train_texts)
    data = pad_sequences(sequences, maxlen=500)
    (X_train,y_train) = (data,train_labels)

    #Fit model to new data and evaluate 
    model.fit(X_train, y_train, epochs=10, batch_size=60)
    acc =  model.evaluate(X_train,y_train)
    return (model,acc)

#TODO there should be only one predict method
def predict_trained_model_path(text,model_path):
    X_predict = np.asarray(text)
    model = load_model(model_path)
    return model.predict_classes(X_predict)


def predict_trained_model(text, model, tokenizer):
    texts = np.asarray(text)
    # cut off the words after seeing 500 words in each document(email)
    max_length = 1000

    sequences = tokenizer.texts_to_sequences(texts)
    data = pad_sequences(sequences, maxlen=max_length)

    X_predict = data
    y_predict = model.predict_classes(X_predict)
    prediction_class = np.array(['true' if i >= 0.5 else 'false' for i in y_predict])

    return prediction_class

if __name__ == "__main__":
    (model,probability) =  train_model('SPAM text message 20170820 - Data.csv','model.h5')
    print(predict_trained_model("hi how are you man",model))
    print(probability)
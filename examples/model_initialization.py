################################################################################
#   Project: ML-tagtog
#   File: model_initialization.py
#   Authors:
#           (c) Uxio Garcia Andrade - uxiog21@gmail.com
#           (c) some random guys in the internet -- TODO findout who
##############################################################################

from keras.layers import SimpleRNN, Embedding, Dense, LSTM
from keras.models import Sequential

import pandas as pd
import numpy as np
import pickle

from keras.layers import SimpleRNN, Embedding, Dense, LSTM
from keras.models import Sequential

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from keras.models import model_from_json

#
#
#

def sentence_processing(texts):

    #limit the number of words in each email
    max_length = 1000

    #Use a tokenizer to process the text data
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)

    #Save the tokenizer
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    #Transform the text list into sequences of the same length
    sequences = tokenizer.texts_to_sequences(texts)
    data = pad_sequences(sequences, maxlen=max_length)

    return data

#Load data
def initialize_and_save_model():
    data = pd.read_csv("spam_messages.csv")

    texts = []
    labels = []

    for i, label in enumerate(data['Category']):
        texts.append(data['Message'][i])
        if label == 'ham':
            labels.append(0)
        else:
            labels.append(1)

    num_rows = len(labels)
    texts = np.asarray(texts)
    labels = np.asarray(labels)

    # number of words used as features
    max_features = 50000

    data = sentence_processing(texts)

    #80% of the data is used for training, the other 20% for testing
    training_samples = int(num_rows * .8)
    validation_samples = int(num_rows - training_samples)
    texts_train = data[:training_samples]
    y_train = labels[:training_samples]
    texts_test = data[training_samples:]
    y_test = labels[training_samples:]

    ##### Build model ####

    model = Sequential()
    model.add(Embedding(max_features, 64))
    model.add(SimpleRNN(64))
    model.add(Dense(1, activation='sigmoid'))

    #Compile the model
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    model.fit(texts_train, y_train, epochs=10, batch_size=50, validation_split=0.2)
    acc = model.evaluate(texts_test, y_test)
    print("The accuracy is {0}".format(acc[1]))

    ##### Save model ####
    #Remember to save the entire model, not just the weights
    model.save("model.h5")
    print("Saved model to disk")

if __name__ == "__main__":
    initialize_and_save_model()
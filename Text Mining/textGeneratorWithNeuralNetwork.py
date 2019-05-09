#-*- coding: utf-8 -*-
# #IMPORT
import sys
from nltk import ngrams
import nltk
from nltk.parse.generate import generate
from nltk import CFG
import pandas as pd
import random
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#VARIABLES
ultimoBigram = []
ultimoTrigram = []
ultimoQuadrigram = []
ultimoPentagram = []
ultimoSeigram = []
ultimoSettegram = []
ultimoTextArr = []
columnnames = ['Album', 'Annoalbum', 'titoloCanzone', 'Secondi', 'testoCanzone', 'significatoTesto']
ultimoText = ""

#BEGIN SCRIPT
ultimoCsv = pd.read_csv("songUltimo.csv", sep=";")
ultimoDf = pd.DataFrame(ultimoCsv)
#print (ultimoDf)

for i in ultimoDf.testoCanzone:
    #ultimoTextArr.append(i)
    i = i.lower()
    ultimoText += " " + i + " "

'''
for ultimoText in ultimoTextArr:
    ultimoBigram.append(list(ngrams(ultimoText.split(), 2)))
    ultimoTrigram.append(list(ngrams(ultimoText.split(), 3)))
    ultimoQuadrigram.append(list(ngrams(ultimoText.split(), 4)))
    ultimoPentagram.append(list(ngrams(ultimoText.split(), 5)))
    ultimoSeigram.append(list(ngrams(ultimoText.split(), 6)))
    ultimoSettegram.append(list(ngrams(ultimoText.split(), 7)))
'''

chars = sorted(list(set(ultimoText)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
n_chars = len(ultimoText)
n_vocab = len(chars)

print ("Total Characters: ", n_chars)
print ("Total Vocab: ", n_vocab)

seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = ultimoText[i:i + seq_length]
	seq_out = ultimoText[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print ("Total Patterns: ", n_patterns)

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
filename = "weights-improvement.hdf5"
print("Model fit")
model.fit(X, y, epochs=30, batch_size=128)
'''
The batch size limits the number of samples to be shown to the network before a weight update can be performed. This same limitation is then imposed when making predictions with the fit model.
Specifically, the batch size used when fitting your model controls how many predictions you must make at a time.
This is often not a problem when you want to make the same number predictions at a time as the batch size used during training.
print("Finish Model fit")
'''
model.save_weights(filename)

# load the network weights
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')

int_to_char = dict((i, c) for i, c in enumerate(chars))
	
# pick a random seed
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print ("Seed:")
print ("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
# generate characters
for i in range(1000):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	x = x / float(n_vocab)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = int_to_char[index]
	seq_in = [int_to_char[value] for value in pattern]
	sys.stdout.write(result)
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print ("\nDone.")

#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160516
Last Modified: 
使用CNN对问句和关系进行分类器训练
'''

import os
import sys

import numpy as np

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Lambda, Merge, Reshape
from keras.layers import Embedding, Input
from keras.layers import Convolution1D
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
from keras import backend as K
from keras.models import Model
from keras.layers import merge

# from CNNTrainData import CNNTrainData

max_features = 100000
time_step = 15
maxlen = 100
batch_size = 100
embedding_dims = 4
nb_filter = 4
filter_length = 2
hidden_dims = 2
nb_epoch = 20

def max_1d(X):
    return K.max(X, axis=1)

def train(train_data, train_relation_data, train_label):
# def train():
    X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
    X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
    print "X_train shape:", X_train.shape
    print "X_test shape:", X_test.shape

    print "Build model...."
    question_model = Sequential()
    question_model.add(Embedding(max_features, embedding_dims
                                input_length=maxlen, dropout=0.2))

    question_model.add(Convolution1D(nb_filter=nb_filter,
                                    filter_length=filter_length,
                                    border_mode="valid",
                                    activation="relu",
                                    subsample_length=1))

    question_model.add(Lambda(max_1d, output_shape=(nb_filter,)))

    relation_model = Sequential()
    relation_model.add(Permute((1, ), input_shape=(embedding_dims, )))

    merged_model = Sequential()
    merged_model.add(Merge([question_model, relation_model], model="concat", concat_axis=1))
    merged_model.add(Dense(1))
    merged_model.add(Activation("sigmoid"))

    rmsprop = RMSPprop(lr=0.1)
    merged_model.compile(loss="binary_crossentropy", optimizer=rmsprop, metrics=["accuracy"])
    merged_model.fit([X_train, X_train_relation], y_train,
                    batch_size=batch_size,
                    nb_epoch=nb_epoch)

    



if __name__ == "__main__":
    word_vector_file = "/users1/ymli/wlj/wordvector/sogou_100_nobinary"
    question_relation_file = "../results/relation/total_train_relations.txt"
    paraphrase_file = "../corpus/paraphrase/mergeallresult.txt"
    focus_file = "../results/focus/focus.txt"

    # class_data = CNNTrainData()
    # class_data.load_classifier_data(word_vector_file, question_relation_file, paraphrase_file, focus_file)

    # train(class_data.train_data, class_data.train_relation_data, class_data.train_label)
    train()
    # test()
    print "Done!"
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
from keras.layers import Dense, Dropout, Activation, Lambda, Merge, Reshape, Permute
from keras.layers import Embedding
from keras.layers import Convolution1D, MaxPooling1D
from keras.optimizers import SGD, RMSprop
from keras.utils import np_utils, generic_utils
from keras import backend as K
from keras.utils.visualize_util import plot


# from CNNTrainData import CNNTrainData


# time_step = 15
time_step = 3
maxlen = 100
# batch_size = 2000
# embedding_dims = 100
# nb_filter = 100
batch_size = 2
embedding_dims = 4
nb_filter = 4
filter_length = 2
hidden_dims = 2
nb_epoch = 1000

def max_1d(X):
    return K.max(X, axis=1)

# def train(train_data, train_relation_data, train_label):
def train():
    X_train = np.array([
        [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]],
        [[2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0]],
        [[3.0, 3.0, 3.0, 3.0], [3.0, 3.0, 3.0, 3.0], [3.0, 3.0, 3.0, 3.0],],
        ])
    X_train_relation = np.array([[1.0, 1.0, 1.0, 1.0], [2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0]])
    y_train = np.array([1, 0, 1])
    # print train_data.shape

    # train_shape = train_relation_data.shape[0]
    # # X_train = train_data[0:int(train_shape*0.9), :]
    # X_train = train_data[0:int(train_shape*0.9)]
    # X_train_relation = train_relation_data[0:int(train_shape*0.9), :]
    # y_train = train_label[0:int(train_shape*0.9)]


    # # X_test = train_data[int(train_shape*0.9):, :]
    # X_test = train_data[int(train_shape*0.9):]
    # X_test_relation = train_relation_data[int(train_shape*0.9):, :]
    # y_test = train_label[int(train_shape*0.9):]

    # print "Pad sequences (samples x time)"
    # X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
    # X_test = sequence.pad_sequences(X_test, maxlen=maxlen)

    # print "X_train shape:", X_train.shape
    # print "X_test shape:", X_test.shape

    print "Build model..."
    question_model = Sequential()
    question_model.add(Convolution1D(
        nb_filter=nb_filter,
        filter_length=filter_length,
        border_mode="valid",
#         activation="relu",
        subsample_length=1,
        input_shape=(time_step, embedding_dims)
        ))

    # question_model.add(Lambda(max_1d, output_shape=(nb_filter,)))
    # question_model.add(MaxPooling1D(pool_length=14))
    question_model.add(Lambda(max_1d, output_shape=(nb_filter,)))

    relation_model = Sequential()
    # relation_model.add(Layer())
    relation_model.add(Permute((1, ), input_shape=(embedding_dims, )))
    # relation_model.add(layer)
    # relation_model.add(Lambda(lambda x: x, input_dim=embedding_dims))
    # relation_model.add(Dense(4, input_dim=4))
    # relation_model.add(Dense(embedding_dims, input_dim=embedding_dims))
    # relation_model.add(Reshape((embedding_dims, ), input_shape=(, embedding_dims)))

    merged_model = Sequential()
    merged_model.add(Merge([question_model, relation_model], mode="concat", concat_axis=1))
    merged_model.add(Dense(1))
    merged_model.add(Activation("sigmoid"))
    plot(merged_model, to_file='model.png', show_shapes=True)
    # return
    rmsprop = RMSprop(lr=0.01)
    # merged_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
    merged_model.compile(loss="binary_crossentropy", optimizer=rmsprop, metrics=['accuracy'])
    merged_model.fit([X_train, X_train_relation], y_train,
        batch_size=batch_size,
        nb_epoch=nb_epoch)

def test():
    model1 = Sequential()
    model1.add(Dense(4, input_dim=4))

    model2 = Sequential()
    model2.add(Dense(4, input_dim=4))

    model = Sequential()
    model.add(Merge([model1, model2], mode="concat", concat_axis=1))
    return
    X_train = np.array([
        [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]],
        [[2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0]],
        [[3.0, 3.0, 3.0, 3.0], [3.0, 3.0, 3.0, 3.0], [3.0, 3.0, 3.0, 3.0],],
        ])
    y_train = np.array([1, 0, 1])
    model = Sequential()
    model.add(Convolution1D(
        nb_filter=nb_filter,
        filter_length=filter_length,
        border_mode="valid",
#        activation="relu",
        subsample_length=1,
        input_shape=(3, 4)
        ))

    model.add(Lambda(max_1d, output_shape=(nb_filter,)))

    # We add a vanilla hidden layer:
    model.add(Dense(hidden_dims))

    model.add(Dense(1))
    model.add(Activation("sigmoid"))

    model.compile(loss="binary_crossentropy",
        optimizer="adam"
        )
    model.fit(X_train, y_train,
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

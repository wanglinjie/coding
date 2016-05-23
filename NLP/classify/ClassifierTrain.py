#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160515
Last Modified: 
对问句和关系进行分类器训练
'''
from __future__ import division
import cPickle
from itertools import izip
import sys
sys.path.append("..")

import numpy as np
from sklearn import svm

from ClassifierData import ClassifierData
from utils.timeutil import Timer

class ClassifierTrain(object):
    def __init__(self):
        self.class_data = None

    def load_train_data(self, word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file):
        '''
        读取所需训练数据
        '''
        self.class_data = ClassifierData()
        self.class_data.load_classifier_data(word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file)


    def train(self, word_vector_file, question_relation_file, paraphrase_file, focus_file, model_file, doubt_words_file):
        '''
        分类模型训练
        '''
        timer = Timer()
        # 导入问句和关系对
        timer.tic()
        self.load_train_data(word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file)
        print "load train data", timer.toc()
        
        train_shape = self.class_data.train_data.shape[0]
        X_train = self.class_data.train_data[0:int(train_shape*0.9), :]
        y_train = self.class_data.train_label[0:int(train_shape*0.9)]

        X_test = self.class_data.train_data[int(train_shape*0.9):, :]
        y_test = self.class_data.train_label[int(train_shape*0.9):]

        print int(train_shape*0.9)
        print "Start train svm model"
        timer.tic()
        clf = svm.SVC(C=4, kernel="rbf")
        # clf = svm.SVC(C=4, kernel="rbf", gamma=0.004)
        # clf = svm.SVC(kernel="sigmoid")
        clf.fit(X_train, y_train)
        f = file(model_file, "w")
        cPickle.dump(clf, f)

        print "Done in train svm model"
        print timer.toc()

        # 预测
        timer.tic()
        print "start predict test data"
        preds = clf.predict(X_test)
        preds_list = list(preds)
        y_list = list(y_test)

        right = 0
        wrong = 0
        real_wrong = 0
        f = open("predict_svm_nopara.txt", "w")
        for pred, real in izip(preds_list, y_list):
            f.write(str(pred) + "\t" + str(real) + "\n")
            if pred == real:
                right += 1
            else:
                wrong += 1
                if real == 1:
                    real_wrong += 1

        print "accuracy: ", right / (right + wrong), right, wrong
        print real_wrong
        print timer.toc()


if __name__ == "__main__":
    '''
    读取问答对
    读取关系
    获取问句的焦点词
    如果问句有焦点词，则获取焦点词的复述
    将问句中的第一个mention替换为空（去掉第一个mention）
    然后对问句进行分词
    将问句焦点词的复述词放在问句后面
    获取问句中每个词的embedding
    将关系输入parse进行分词
    获取关系分词后词的embedding
    利用问句embedding和关系embedding进行训练分类器
    '''
    word_vector_file = "/users1/ymli/wlj/wordvector/sogou_100_nobinary"
    # word_vector_file = "/users1/ymli/wlj/wordvector/giga-50.bin"
    question_relation_file = "../results/relation/total_train_relations3.txt"
    # wrong_relation_file = "../results/relation/wrong_train_relations2.txt"
    paraphrase_file = "../corpus/paraphrase/mergeallresult.txt"
    focus_file = "../results/focus/focus.txt"
    doubt_words_file = "../rule/questionwords.txt"

    # model_file = "svm_nopara_model.txt"
    model_file = "./model/svm_sogou_newtrain.model"
    classifier = ClassifierTrain()
    classifier.train(word_vector_file, question_relation_file, paraphrase_file, focus_file, model_file, doubt_words_file)
    print "Done!"
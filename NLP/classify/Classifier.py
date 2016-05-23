#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160515
Last Modified: 
对问句和关系进行分类判断
'''
from __future__ import division
import cPickle
from itertools import izip
import sys
sys.path.append("..")

import numpy as np
from sklearn import svm

from data.Focus import Focus
from data.WordParaphrase import WordParaphrase
from data.wordvector import WordVectors
from utils.Parse import Parsing
from utils.timeutil import Timer


class Classifier(object):
    def __init__(self, model_file, word_vector_file, focus_file, paraphrase_file, doubt_words_file):
        self._parse = Parsing()
        self.word_vectors = None
        self.focus = None
        self.word_para = None
        self.doubt_words = None

        self.classifier = None

        self.load_classifier(model_file)
        self.load_resource(word_vector_file, focus_file, paraphrase_file, doubt_words_file)

    def load_resource(self, word_vector_file, focus_file, paraphrase_file, doubt_words_file):
        '''
        '''
        print "start load word vectors"
        self.word_vectors = WordVectors.load_vectors(word_vector_file)
        print "Done: load word vectors"
        print "load question focus"
        self.focus = Focus.load_focus(focus_file)
        print "load word paraphrase"
        self.word_para = WordParaphrase.load_word_paraphrase(paraphrase_file)
        # return focus, word_para
        print "load question words"
        doubt_words = []
        with open(doubt_words_file, "r") as r:
            for line in r:
                word = line.strip()
                doubt_words.append(word)
        self.doubt_words = doubt_words

    def get_embedding(self, word):
        '''
        获取一个字的embedding
        '''
        word_index = self.word_vectors.get_word_index(word)
        if word_index:
            word_vector = self.word_vectors[word_index]
        else:
            # print word, "no embedding"
            word_vector = np.zeros(self.word_vectors._embsize)
        return word_vector

    def get_words_embedding(self, words):
        words_embed = np.zeros(self.word_vectors._embsize)
        for i, word in enumerate(words):
            word_vector = self.get_embedding(word)
            if i:
                words_embed += word_vector
            else:
                words_embed = word_vector
        if len(words):
            words_embed /= float(len(words))
        # if np.isinf(words_embed)[0]:
        #     print "infs ", words[0]
        return words_embed


    def load_classifier(self, model_file):
        '''
        加载分类模型
        '''
        f = open(model_file, "r")
        self.classifier = cPickle.load(f)

    def add_paraphrase(self, question, mention):
        '''
        添加问句焦点词的复述
        '''
        # 移除问句中疑问词
        # for word in self.doubt_words:
        #     if word in question:
        #         question = question.replace(word, "")

        # question = question.replace(mention, "")
        question = question.strip("？")
        focus_word = self.focus.get_question_focus(question)
        if focus_word:
            focus_paraphrase = self.word_para.get_word_paraphrase(focus_word)
            if focus_paraphrase:
        #         for i in focus_paraphrase:
        #             question += i
                    question += focus_paraphrase[0]
        return question

    def classify(self, question, relation, mention):
        '''
        return:Bool
        '''
        question = self.add_paraphrase(question, mention)
        question_words = self._parse.segment(question)
        relation_words = self._parse.segment(relation)

        question_embedding = self.get_words_embedding(question_words)
        relation_embedding = self.get_words_embedding(relation_words)

        question_relation = []
        question_relation.append(np.concatenate((question_embedding, relation_embedding)))

        preds = self.classifier.predict(question_relation)
        preds_list = list(preds)
        return preds_list[0]


if __name__ == "__main__":
    word_vector_file = "/users1/ymli/wlj/wordvector/sogou_100_nobinary"
    focus_file = "../results/focus/focus.txt"
    paraphrase_file = "../corpus/paraphrase/mergeallresult.txt"
    doubt_words_file = "../rule/questionwords.txt"

    # model_file = "sigmoid_svm_nopara_model.txt"
    model_file = "svm_embedding_model.txt"

    classifier = Classifier(model_file, word_vector_file, focus_file, paraphrase_file, doubt_words_file)
    input_string = raw_input("请输入问句以及关系")
    while input_string != "exit":
        input_string_list = input_string.split()
        if len(input_string_list) != 2:
            input_string = raw_input("请输入问句以及关系：")
            continue


        question = input_string_list[0]
        relation = input_string_list[1]
        if classifier.classify(question, relation, ""):
            print "yes"
        else:
            print "no"
        input_string = raw_input("请输入问句以及关系：")
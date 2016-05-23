#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160517
Last Modified: 
获取问句和关系CNN分类训练数据
'''
import copy
import sys
sys.path.append("..")

import numpy as np

from data.QuestionRelation import QuestionRelation
from data.Focus import Focus
from data.WordParaphrase import WordParaphrase
from data.wordvector import WordVectors
from utils.Parse import Parsing

input_length = 15

class CNNTrainData(object):
    def __init__(self):
        self._parse = Parsing()
        self.word_vectors = None

        self.train_data = None
        self.train_relation_data = None
        self.train_label = None
        
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
        words_embed = []
        for word in words:
            word_vector = self.get_embedding(word)
            words_embed.append(word_vector)
            # words_embed.append(word_vector.tolist())
            # if i:
            #     words_embed += word_vector
            # else:
            #     words_embed = word_vector
        return words_embed

    def get_relation_embedding(self, words):
        words_embed = np.zeros(self.word_vectors._embsize)
        for i, word in enumerate(words):
            word_vector = self.get_embedding(word)
            # words_embed.append(word_vector)
            if i:
                words_embed += word_vector
            else:
                words_embed = word_vector
        return copy.deepcopy(words_embed)


    def load_resource(self, word_vector_file, question_relation_file, paraphrase_file, focus_file):
        '''
        加载其它资源
        '''
        print "start load word vectors"
        self.word_vectors = WordVectors.load_vectors(word_vector_file)
        print "Done: load word vectors"
        print "start load question relation"
        que_rela = QuestionRelation.load_question_relation(question_relation_file, "")
        print "load question focus"
        focus = Focus.load_focus(focus_file)
        print "load word paraphrase"
        word_para = WordParaphrase.load_word_paraphrase(paraphrase_file)
        return que_rela, focus, word_para

    def add_paraphrase(self, que_relas, focus, word_para):
        '''
        添加问句焦点词的复述
        '''
        que_para_relas = []
        for question_relation in que_relas.question_relation_pair:
            question = question_relation[0]
            mention = question_relation[1]
            label = question_relation[3]

            question = question.replace(mention, "")
            question = question.strip("？")
            focus_word = focus.get_question_focus(question)
            if focus_word:
                focus_paraphrase = word_para.get_word_paraphrase(focus_word)
                for i in focus_paraphrase:
                    question += i
                # if focus_paraphrase: 
                #     question += focus_paraphrase[0]
            
            que_para_relas.append([question, question_relation[2], label])
        return que_para_relas


    def load_classifier_data(self, word_vector_file, question_relation_file, paraphrase_file, focus_file):
        '''
        加载分类器训练数据
        '''
        train_embedding = []
        train_relation_embedding = []
        train_label = []

        que_relas, focus, word_para = self.load_resource(word_vector_file, question_relation_file, paraphrase_file, focus_file)
        que_para_relas = self.add_paraphrase(que_relas, focus, word_para)

        # num = 0
        # 将问句分词，获取词向量
        for question_relation in que_para_relas:
            question = question_relation[0]
            relation = question_relation[1]
            label = question_relation[2]
            question_words = self._parse.segment(question)
            relation_words = self._parse.segment(relation)

            # padding

            question_embedding = self.get_words_embedding(question_words)
            # question_embedding = self.get_relation_embedding(question_words)
            relation_embedding = self.get_relation_embedding(relation_words)

            if len(question_embedding) < input_length:
                for i in xrange(input_length-len(question_embedding)):
                    # question_embedding.append([0] * self.word_vectors._embsize)
                    question_embedding.append(np.zeros(self.word_vectors._embsize))
            elif len(question_embedding) > input_length:
                # for i in xrange(input_length-len(question_words), -1, -1):
                del question_embedding[0:(len(question_embedding)-input_length)]

            if len(question_embedding) != input_length:
                print question, "don't have right length", len(question_embedding)
            train_embedding.append(question_embedding)
            train_relation_embedding.append(relation_embedding)
            # train_embedding.append(np.concatenate((question_embedding, relation_embedding)))
            train_label.append(int(label))
            # num += 1
            # if num > 3000:
            #     break

        # print train_embedding[0].shape
        # print len(train_embedding[0][0])
        # print train_embedding[0][0].shape
        # print np.array(train_embedding).shape
        # print np.array(train_embedding)[0].shape
        self.train_data = np.array(train_embedding)
        self.train_relation_data = np.array(train_relation_embedding)
        self.train_label = np.array(train_label)
        
        # print self.train_data[0:]
        # print self.train_data[0]
        # print self.train_data.shape
        # print self.train_data.shape[0]
        # print self.train_data.shape[1]
        # print self.train_data.shape[2]
        # print self.train_label.shape
        # print self.train_relation_data.shape
        # self.train_data = self.train_data.reshape((self.train_data.shape[0], 15, 100))
        # print self.train_data.shape
        assert(self.train_data.shape[0] == self.train_label.shape[0])



if __name__ == "__main__":
    word_vector_file = "/users1/ymli/wlj/wordvector/sogou_100_nobinary"
    question_relation_file = "../results/relation/total_train_relations.txt"
    paraphrase_file = "../corpus/paraphrase/mergeallresult.txt"
    focus_file = "../results/focus/focus.txt"

    class_data = CNNTrainData()
    class_data.load_classifier_data(word_vector_file, question_relation_file, paraphrase_file, focus_file)
    # import numpy as np
    # embedding = []
    # for i in xrange(22856):
    #     embedding1 = []
    #     for j in xrange(15):
    #         embedding1.append([0] * 100)
    #     embedding.append(embedding1)
    # result = np.array(embedding)
    # print result.shape
    print "Done!"
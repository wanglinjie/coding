#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160515
Last Modified: 
获取问句和关系分类训练数据
'''
import sys
sys.path.append("..")

import numpy as np

from data.QuestionRelation import QuestionRelation
from data.Focus import Focus
from data.WordParaphrase import WordParaphrase
from data.wordvector import WordVectors
from utils.Parse import Parsing

class ClassifierData(object):
    def __init__(self):
        self._parse = Parsing()
        self.word_vectors = None

        self.train_data = None
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
        words_embed = np.zeros(self.word_vectors._embsize)
        for i, word in enumerate(words):
            word_vector = self.get_embedding(word)
            if i:
                words_embed += word_vector
            else:
                words_embed = word_vector
        # words_embed /= float(len(words))
        if len(words):
            words_embed = words_embed / float(len(words))

        return words_embed

    def load_resource(self, word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file):
        '''
        加载其它资源
        '''
        print "start load word vectors"
        self.word_vectors = WordVectors.load_vectors(word_vector_file)
        print "Done: load word vectors"
        print "start load question relation"
        que_rela = QuestionRelation.load_question_relation(question_relation_file)
        print "load question focus"
        focus = Focus.load_focus(focus_file)
        print "load word paraphrase"
        word_para = WordParaphrase.load_word_paraphrase(paraphrase_file)
        print "load question words"
        doubt_words = []
        with open(doubt_words_file, "r") as r:
            for line in r:
                word = line.strip()
                doubt_words.append(word)

        return que_rela, focus, word_para, doubt_words

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
                if focus_paraphrase: 
                    question += focus_paraphrase[0]
            
            que_para_relas.append([question, question_relation[2], label])
        return que_para_relas

    def remove_doubt_words(self, question, doubt_words):
        '''
        移除问句中疑问词
        '''
        for word in doubt_words:
            if word in question:
                question = question.replace(word, "")
        return question


    def load_classifier_data(self, word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file):
        '''
        加载分类器训练数据
        '''
        train_embedding = []
        train_label = []

        que_relas, focus, word_para, doubt_words = self.load_resource(word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file)
        que_para_relas = self.add_paraphrase(que_relas, focus, word_para)

        # 将问句分词，获取词向量
        for question_relation in que_para_relas:
            question = question_relation[0]
            relation = question_relation[1]
            label = question_relation[2]

            # question = self.remove_doubt_words(question, doubt_words)
            question_words = self._parse.segment(question)
            relation_words = self._parse.segment(relation)

            question_embedding = self.get_words_embedding(question_words)
            relation_embedding = self.get_words_embedding(relation_words)

            train_embedding.append(np.concatenate((question_embedding, relation_embedding)))
            # train_embedding.append(np.concatenate((relation_embedding, question_embedding)))
            # train_embedding.append(question_embedding-relation_embedding)
            train_label.append(int(label))
            # train_label.append(int(label))

        self.train_data = np.array(train_embedding)
        self.train_label = np.array(train_label)
        assert(self.train_data.shape[0] == self.train_label.shape[0])



if __name__ == "__main__":
    word_vector_file = "/users1/ymli/wlj/wordvector/sogou_100_nobinary"
    question_relation_file = "../results/relation/total_train_relations.txt"
    # wrong_relation_file = "../results/relation/wrong_train_relations2.txt"
    paraphrase_file = "../corpus/paraphrase/mergeallresult.txt"
    focus_file = "../results/focus/focus.txt"
    doubt_words_file = "../rule/questionwords.txt"

    class_data = ClassifierData()
    class_data.load_classifier_data(word_vector_file, question_relation_file, paraphrase_file, focus_file, doubt_words_file)
    print "Done!"
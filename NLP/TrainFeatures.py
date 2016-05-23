#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160507
Last Modified: 
获取训练数据输入的特征
'''

from QuestionFeature import QuestionFeature

class TrainFeatures(object):
    def __init__(self):
        self.que_fea = QuestionFeature()

        self.features_space = []


    def get_train_features(self):
        # 读取问句、答案、实体、关系

        # 输入问句、实体，获取问句特征
        question_features, question_label = self.que_fea.get_question_feature(question)

        # 输入关系、答案，获取三元组特征

        # 结合问句特征和三元组特征作为特征输入





if __name__ == "__main__":
    pass
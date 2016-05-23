#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160504
Last Modified: 
KBQA(knowledge based question answer)
'''

from QuestionFeature import Feature
from Knowledge import Knowledge

class KBQA(object):
    def __init__(self, lexicon_path=""):
        self._feature = Feature(lexicon_path)

    def run(self):
        # 加载训练数据，问句实体事先获取

        # 问题分类
        question = "王娟是男性还是女性"

        # 特征提取

        # 分类模型训练

        #


if __name__ == "__main__":
    '''
    读取问句
    实体识别
    相关知识抽取
    问句分类（不同类型问句不同处理）
        选择型的问句直接使用规则或者字符串匹配等回答
        特指问句使用分类器进行分类
    从相应知识中抽取答案
    '''
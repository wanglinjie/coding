#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 201605014
Last Modified: 
读取词复述资源
'''
import os

class WordParaphrase(object):
    def __init__(self):
        self.word_paraphrase = {}

    @classmethod
    def load_word_paraphrase(cls, filepath):
        '''
        filepath:复述资源文件路径
        加载复述资源
        '''
        if not os.path.isfile(filepath):
            print "{0} not exist!\n".format(filepath)
            raise IOError
        paraphrase = {}
        with open(filepath, "r") as r:
            for line in r:
                line_split = line.strip().split()
                if len(line_split) < 2:
                    continue
                if line_split[0] not in paraphrase:
                    paraphrase[line_split[0]] = line_split[1:]
                else:
                    paraphrase[line_split[0]].extend(line_split[1:])
        word_para = WordParaphrase()
        word_para.word_paraphrase = paraphrase
        return word_para

    def get_word_paraphrase(self, word):
        '''
        word:需要获取复述的词
        获取词的复述
        '''
        if word in self.word_paraphrase:
            # 如果有该词的复述，则直接返回复述结果
            return self.word_paraphrase[word]
        else:
            # 如果没有则需要遍历复述结果查找
            for i in self.word_paraphrase:
                if word in self.word_paraphrase[i]:
                    return [i]
            return []


if __name__ == "__main__":
    filepath = "../../paraphrase/infobox/results/mergeallresult.txt"
    word_para = WordParaphrase.load_word_paraphrase(filepath)
    result = word_para.get_word_paraphrase("甚为")
    if not result:
        print "no result"
    for i in result:
        print i
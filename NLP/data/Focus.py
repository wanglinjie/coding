#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160515
Last Modified: 
读取问句focus
'''
import os
class Focus(object):
    def __init__(self):
        # key为question，value为问句focus
        self.question_focus = {}

    
    # def load_focus(self, focus_file, polite_file=""):
    @classmethod
    def load_focus(cls, focus_file, polite_file=""):
        question_focus = {}
        if not polite_file:
            polite_file = "../rule/polite.txt"
        if not os.path.isfile(focus_file):
            print "{0} file not exist!".format(focus_file)
            raise IOError
        if not os.path.isfile(polite_file):
            print "{0} file not exist!".format(polite_file)
            raise IOError

        # 读取客气词
        polite_words = []
        with open(polite_file, "r") as r:
            for line in r:
                word = line.strip()
                polite_words.append(word)

        # 读取问句以及焦点词
        with open(focus_file, "r") as r:
            line_num = 0
            for line in r:
                line_num += 1
                line_split = line.strip().split("\t")
                if len(line_split) < 3:
                    # print line_num
                    continue
                question = line_split[0]
                for i in polite_words:
                    if i in question:
                        question = question.replace(i, "")
                question = question.replace(" ", "")
                topic = line_split[2]
                # self.question_focus[question] = topic
                question_focus[question] = topic

        focus = Focus()
        focus.question_focus = question_focus
        return focus

    def get_question_focus(self, question):
        '''
        获取问句的focus
        '''
        if question in self.question_focus:
            return self.question_focus[question]
        else:
            return ""



if __name__ == "__main__":
    focus_file = "../results/focus/focus.txt"
    focus = Focus.load_focus(focus_file)
    # focus = Focus()
    # focus.load_focus(focus_file)
    print "hello", focus.question_focus["海信led39k370x3d的背光灯是什么类型？"]
    for i in focus.question_focus:
        print i
        print focus.question_focus[i]
        break
    print "Done!"
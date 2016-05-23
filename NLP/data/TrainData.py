#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160427
Last Modified: 
获取训练数据
'''

class TrainData(object):
    def __init__(self, train_file, polite_file):
        self.train_file = train_file
        self.polite_file = polite_file

        # self.train_data = {}
        self.train_data = []
        self.polite_words = []


    def get_politewords(self):
        # 读取客气词
        with open(self.polite_file, "r") as r:
            for line in r:
                self.polite_words.append(line.strip())


    def preprocess(self, question):
        # 去除问句中客气词
        for i in self.polite_words:
            if i in question:
                return question.replace(i, "")
        return question

    def get_data(self):
        '''
        读取训练数据
        '''
        self.get_politewords()

        num = 0
        key = ""
        number = 0
        with open(self.train_file, "r") as r:
            for line in r:
                if line.startswith("=================================================="):
                    continue
                # line = line.replace(" ", "")
                line_split = line.strip().split("\t")
                if len(line_split) < 2:
                    print line
                    num += 1
                    num %= 2
                    continue
                # line_split[1] = line_split[1].replace(" ", "")
                if num:
                    if key:
                        # if key in self.train_data:
                        #     print "have", key
                        # number += 1
                        # self.train_data[key] = line_split[1]
                        # key = ""
                        self.train_data.append((key, line_split[1]))
                    else:
                        print "error empty key"
                else:
                    # 
                    key = self.preprocess(line_split[1])
                    key = key.replace(" ", "")
                    # print key
                    if not key:
                        print "empty key"
                num += 1
                num %= 2
        print len(self.train_data)
        with open("./results/train.txt", "w") as w:
            for i in self.train_data:
                # w.write(i + "\t" + self.train_data[i] + "\n")
                w.write(i[0] + "\t" + i[1] + "\n")
        print number


def train_test_data():
    import random
    rfile = u"../../../QA/评测/NLPCC2016QA.评测工具包/NLPCC2016QA/training/nlpcc-iccpol-2016.kbqa.training-data"
    train_file = "./results/train_data.txt"
    test_file = "./results/test_data.txt"
    test_num = 3000
    with open(rfile, "r") as r, open(train_file, "w") as wtrain, open(test_file, "w") as wtest:
        num = 0
        data = ""
        for line in r:
            if line.startswith("============"):
                data += line
                temp = random.randint(0, 1)
                if (not temp) and (num < test_num):
                    wtest.write(data)
                    num += 1
                else:
                    wtrain.write(data)
                data = ""
            else:
                data += line

def get_train_negative_relation():
    rfile = "../results/relation/right_train_relations.txt"
    wfile = "../results/relation/wrong_train_relations2.txt"

    with open(rfile, "r") as r, open(wfile, "w") as w:
        num = 0
        key = "中文名\t别名\n"
        line_num = 0
        key_list = []
        for line in r:
            line_num += 1
            if line.startswith("------"):
                w.write(line)
                continue
            if num:
                w.write(key)
                key_list.append(line)
                if line_num > 2:
                    key = key_list[0]
                    if not key.strip():
                        key = "别名\n"
                    del key_list[0]

            else:
                w.write(line)
            num += 1
            num %= 2




if __name__ == "__main__":
    train_file = u"../../../QA/评测/NLPCC2016QA.评测工具包/NLPCC2016QA/training/nlpcc-iccpol-2016.kbqa.training-data"
    # polite_file = u"../results/polite.txt"
    # train_file = "./results/train_data.txt"
    # polite_file = u"../utils/客气词.txt"
    polite_file = "../rule/polite.txt"

    # train = TrainData(train_file, polite_file)
    # train.get_data()
    # train_test_data()
    get_train_negative_relation()
    print "Done!"
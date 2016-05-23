#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160427
Last Modified: 
利用训练数据中问题和答案来确定具体知识，并提取知识中关系
'''
import sys
sys.path.append("..")

# from TrainData import TrainData
from Knowledge import Knowledge


class Relation(object):
    def __init__(self, name2idpath, triplepath, question2idfile, relation_file):
        self.name2idpath = name2idpath
        self.triplepath = triplepath
        self.question2idfile = question2idfile
        self.relation_file = relation_file

    def get_train_relation(self):

        # name2idpath = "../corpus/nlpcc-iccpol-2016.kbqa.kb.mention2id"
        # triplepath = "../corpus/nlpcc-iccpol-2016.kbqa.kb"
        know = Knowledge(self.name2idpath, self.triplepath)
        print "Start: load name 2 id"
        know.load_name2id()
        print "Done: load name2id"
        print "Start: load triple"
        know.load_triple()
        print "Done: load triple"

        # question2idfile = ""
        f = open("temp.txt", "w")
        with open(self.question2idfile, "r") as r, open(self.relation_file, "w") as w:
            for line in r:
                line_split = line.strip().split("\t")
                # if len(line_split) != 3:
                #     continue


                question = line_split[0]
                answer = line_split[1]
                entrys = line_split[2:]

                
                relations = set()
                for entry in entrys:
                    # 查找对应ID
                    ids = know.GetEntityIdByName(entry.decode("utf-8"))
                    if len(ids) == 0:
                        f.write(question + "\t" + entry + '\n')
                    for i in ids:
                        relation = know.GetWrongRelation(i, answer.decode("utf-8"))
                        # if len(relation) > 1:
                        #     print "error more than 1 relation", line.strip(), relation
                        if len(relation):
                            relations.add(relation[0])

                # relations = list(set(relations))
                relations = list(relations)
                w.write("-------------------\n")
                w.write(line.strip() + "\n")
                # if len(relations) > 1:
                #     print "more than 1 relation", line.strip(), relations
                # if len(relations) == 0:
                #     print

                # for i in relations:
                #     w.write("\t" + i.encode("utf-8"))
                w.write(relations[0].encode("utf-8"))
                w.write("\n")


def get_train_data_relation():
    relation_file = "../results/get_train_relation.txt"
    all_data_file = "./results/train.txt"
    train_file = "../results/matchentity/train_filter_by_ner_count.txt"

    result_file = "../results/relation/wrong_train_relations2.txt"

    relations = []
    with open(relation_file, "r") as r:
        num = 0
        for line in r:
            if line.startswith("---"):
                continue
            num += 1
            num %= 2
            if not num:
                relations.append(line.strip())
    print len(relations)
    question_2_relation = {}
    with open(all_data_file, "r") as r:
        num = 0
        for line in r:
            line_split = line.strip().split("\t")
            question_2_relation[line_split[0]] = num
            num += 1
    with open(train_file, "r") as r, open(result_file, "w") as w:
        for line in r:
            line_split = line.strip().split("\t")
            question = line_split[0]
            if question in question_2_relation:
                w.write(line)
                w.write(relations[question_2_relation[question]] + "\n")
                w.write("-------------------------------\n")
            else:
                print line



if __name__ == "__main__":
    name2idpath = "../corpus/nlpcc-iccpol-2016.kbqa.kb.mention2id"
    triplepath = "../corpus/nlpcc-iccpol-2016.kbqa.kb"
    question2idfile = "../results/matchentity/train_filter_by_ner_count.txt"
    relation_file = "../results/relation/wrong_train_relations2.txt"

    rela = Relation(name2idpath, triplepath, question2idfile, relation_file)
    rela.get_train_relation()
    # get_train_data_relation()
    pass
#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160515
Last Modified: 
读取问句和关系对
'''

class QuestionRelation(object):
    def __init__(self):
        self.question_relation_pair = []

    @classmethod
    def load_question_relation(cls, filepath):
        '''
        加载问句和关系对
        '''
        question_relation = []

        # with open(wrong_relation_file, "r") as r:
        #     num = 0
        #     line_num = 0
        #     question = ""
        #     mention = ""
        #     for line in r:
        #         line_num += 1
        #         if line.startswith("---"):
        #             continue
        #         line_split = line.strip().split("\t")
        #         num += 1
        #         num %= 2
        #         if num:
        #             if len(line_split) < 3:
        #                 print line_num, line, "less than three element"
        #             question = line_split[0]
        #             mention = line_split[2]
        #         else:
        #             if line.strip() and question:
        #                 for i in line_split:
        #                     question_relation.append([question, mention, i, 0])
        #             question = ""
        #             mention = ""

        with open(filepath, "r") as r:
            line_num = 0
            num = 0
            right_wrong = 0
            question = ""
            mention = ""
            for line in r:
                line_num += 1
                if line.startswith("---"):
                    continue
                line_split = line.strip().split("\t")
                num += 1
                num %= 2
                if num:
                    if len(line_split) < 3:
                        print line_num, line, "less than three element"
                    question = line_split[0]
                    mention = line_split[2]
                else:
                    right_wrong += 1
                    right_wrong %= 2
                    if line.strip() and question:
                        for i in line_split:
                            question_relation.append([question, mention, i, right_wrong])
                    else:
                        # print line_num, question, "no relation"
                        pass
                    question = ""
                    mention = ""
        

        que_rela = QuestionRelation()
        que_rela.question_relation_pair = question_relation
        return que_rela

def merge_right_wrong_relation():
    from itertools import izip
    right_relation_file = "../results/relation/right_train_relations.txt"
    wrong_relation_file = "../results/relation/wrong_train_relations3.txt"
    total_train_file = "../results/relation/total_train_relations3.txt"
    # relations_file = [right_relation_file, wrong_relation_file]
    right_relation_lines = []
    wrong_relation_lines = []
    with open(right_relation_file, "r") as r:
        lines = ""
        for line in r:
            lines += line
            if line.startswith("---"):
                right_relation_lines.append(lines)
                lines = ""
    with open(wrong_relation_file, "r") as r:
        lines = ""
        for line in r:
            lines += line
            if line.startswith("---"):
                wrong_relation_lines.append(lines)
                lines = ""

    with open(total_train_file, "w") as w:
        for i, j in izip(right_relation_lines, wrong_relation_lines):
            w.write(i)
            w.write(j)





if __name__ == "__main__":
    # filepath = "../results/relation/right_train_relations.txt"
    # wrong_relation_file = "../results/relation/wrong_train_relations2.txt"
    # que_rela = QuestionRelation.load_question_relation(filepath, wrong_relation_file)
    merge_right_wrong_relation()
    print "Done!"
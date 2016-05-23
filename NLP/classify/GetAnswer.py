#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 201605016
Last Modified: 
抽取答案，并对答案排序
'''



def answer_format():
    # 将预测结果改写成评测格式
    test_data_file = u"../data/results/test_data.txt"
    rfile = "./results/predicted_answers_svm_rule_newtrain2.txt"
    wfile = "./results/predicted_answers_format_svm_rule_newtrain2.txt"

    # rfile = "../embeddingtest/results/simi_predicted_answers_test.txt"
    #  wfile = "../embeddingtest/results/simi_predicted_format_answers_test.txt"


    # question_head = "<question id={0}>"
    # answer_head = "<answer id={0}>"
    segmentation = "=================================================="


    train_questions = []
    with open(test_data_file, "r") as r:
        num = 0
        data = []
        for line in r:
            if line.startswith("===="):
                continue
            num += 1
            num %= 2
            if num:
                data.append(line)
                # line_split = line.strip().split("\t")
                # if len(line_split) != 2:
                #     train_questions.append("")
                # else:
                #     train_questions.append(line_split[1])
            else:
                line_split = line.strip().split("\t")
                data.append(line_split[0])
                train_questions.append(data)
                data = []

    with open(rfile, "r") as r, open(wfile, "w") as w:
        line_num = 0
        num = 0
        for line in r:
            if line.startswith("---"):
                num = 0
                continue
            if num:
                line_split = line.strip().split("\t")
                if len(line_split) < 3:
                    answer = ""
                else:
                    answer = line_split[2]
                w.write("\t" + answer)
            else:
                w.write("\n")
                w.write(segmentation + "\n")
                # w.write(question_head.format(line_num+1)+ "\t" + train_questions[line_num] + "\n")
                w.write(train_questions[line_num][0])
                w.write(train_questions[line_num][1])
                # w.write(answer_head.format(line_num+1))
                line_num += 1
            num += 1
        w.write("\n" + segmentation)

def remove_duplicate():
    # 去除答案中重复项
    rfile = "./results/predicted_answers_format_svm_rule_newtrain2.txt"
    wfile = "./results/predicted_answers_format_svm_distinct_rule_newtrain2.txt"
    # rfile = "../embeddingtest/results/simi_predicted_format_answers_test.txt"
    # wfile = "../embeddingtest/results/simi_predicted_format_distinct_answers_test.txt"

    with open(rfile, "r") as r, open(wfile, "w") as w:
        num = 0
        for line in r:
            num += 1
            num %= 3
            if num != 2:
                w.write(line)
            else:
                line_split = line.strip().split("\t")
                if len(line_split) < 2:
                    w.write(line_split[0] + "\t" + " \n")
                else:
                    answers = []
                    for i in line_split[1:]:
                        if i not in answers:
                            answers.append(i)
                    w.write(line_split[0])
                    for i in answers:
                        w.write("\t" + i)
                    w.write("\n")


if __name__ == "__main__":
    # answer_format()
    remove_duplicate()
    print "Done!"
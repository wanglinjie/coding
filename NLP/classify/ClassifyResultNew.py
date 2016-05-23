#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160522
Last Modified: 
新添加内容
对问句和关系进行分类判断存储结果
'''

import sys
sys.path.append("..")
# from scipy import linalg, mat, dot
import numpy as np

from Classifier import Classifier
# from wordvector import WordVectors
# from utils.Parse import Parsing
from Knowledge import Knowledge
from QuestionFeature import QuestionFeature


class ClassifyResult(object):
    def __init__(self, classifier, name2idpath, triplepath, question2idfile, answer_file):
        self.classifier = classifier

        self.questionfeature = QuestionFeature()

        self.name2idpath = name2idpath
        self.triplepath = triplepath
        self.question2idfile = question2idfile
        self.answer_file = answer_file

        self.know = Knowledge(self.name2idpath, self.triplepath)


    def load_resource(self):
        print "Start: load name2id"
        self.know.load_name2id()
        print "Done: load name2id"
        print "Start: load triple"
        self.know.load_triple()
        print "Done: load triple"

    def have_same_word(self, question_words, id_words):
        '''
        判断id中是否有和问句重合的词
        return:bool
        '''
        for i in id_words:
            if i in question_words:
                return True
        return False

    def get_yes_relation(self, features, relation_answer):
        '''
        根据问句中抽取的特征和关系、答案是否有重叠字判断
        features:问句中特征拼接的字符串
        return:bool
        '''
        if self.have_same_word(list(relation_answer), list(features)):
            return True
        else:
            return False

    def after_yes(self, question, question_label, mention):
        '''
        判断mention是否在关键词后
        '''
        if question_label == 2:
            key_index = question.index("还是")
            
        else:
            key_index = question.index("是不是")
        if question.index(mention) > key_index:
            return True
        else:
            return False

    def compute_similar(self, a, b):
        '''
        计算相似性
        '''
        # if np.isinf(b.any()):
        #     print "b inf"
        # if np.isinf(a.any()):
        #     print "a inf", question
        #     return -1
        try:
            c = np.dot(a, b)/np.linalg.norm(a)/np.linalg.norm(b)
        except:
            c = -1
            # print a, question
        return c

    def question_relation_similar(self, question, relation, mention):
        '''
        '''
        question = question.replace(mention, "")
        question = question.strip("？")
        question_words = self.classifier._parse.segment(question)
        question_embedding = self.classifier.get_words_embedding(question_words)


        relation_words = self.classifier._parse.segment(relation)
        relation_embedding = self.classifier.get_words_embedding(relation_words)

        similarity = self.compute_similar(question_embedding, relation_embedding)
        return similarity


    def run(self):
        self.load_resource()
        with open(self.question2idfile, "r") as r, open(self.answer_file, "w") as w:
            for line in r:
                relation_names = []

                # 记录使用分类器分类获取得到的三元组
                predicted_answers = []

                #记录使用问句embedding和关系embedding相似性获取得到的三元组
                predict_similar_answers = []

                # 记录关系和问句中重叠字的三元组
                predicted_sameword_answers = []

                # question_embedding = np.zeros(self.classifier.word_vectors._embsize)

                line_split = line.strip().split("\t")
                if len(line_split) < 3:
                    print line, "no entity"
                    continue

                question = line_split[0]
                answer = line_split[1]
                mentions = line_split[2:]

                question_features, question_label = self.questionfeature.get_question_feature(question, mentions[0:1])

                question_words = list(question.decode("utf-8"))
                question_no_first_mention = question.replace(mentions[0], "")
                question_no_first_mention_words = list(question_no_first_mention.decode("utf-8"))

                for mention in mentions:

                    # 如果实体出现在“是不是”、“还是”之后，则丢弃
                    if question_label != 1:
                        if self.after_yes(question, question_label, mention):
                            continue

                    # 查找对应的ID
                    ids = self.know.GetEntityIdByName(mention.decode("utf-8"))
                    for i in ids:

                        max_similar = 0
                        predict_similar_answer = None

                        id_words = list(i)

                        # 判断id中是否有和问句重合的词
                        if not self.have_same_word(question_words, id_words):
                            continue

                        knowledges = self.know.GetPredicatesByEntityId(i)
                        predicted_answer = []
                        # predicted_sameword_answer = []
                        for relation in knowledges:

                            # 处理选择问句
                            if question_label != 1:
                                triple_object = "".join(knowledges[relation])
                                relation_answer = relation + triple_object
                                if self.get_yes_relation(question_features.decode("utf-8"), relation_answer):
                                    for j in knowledges[relation]:
                                        predicted_answer.append([i.encode("utf-8"), relation.encode("utf-8"), j.encode("utf-8")])
                                        # predicted_sameword_answer.append([i.encode("utf-8"), relation.encode("utf-8"), j.encode("utf-8")])
                                continue

                            # id和关系是完全一样的，则丢弃这种结果
                            if (relation in i):
                                continue
                            # if (relation in i) and (len(list(relation)) != 1):
                            #     continue

                            # 如果关系完整出现在问句中，则该id只保留该三元组
                            if relation.encode("utf-8") in question:
                                # if len(list(relation)) == 1:
                                #     print relation.encode("utf-8"), question
                                # predicted_answer = []
                                for j in knowledges[relation]:
                                    if relation.encode("utf-8") not in relation_names:
                                        relation_names.append(relation.encode("utf-8"))
                                    predicted_answer.append([i.encode("utf-8"), relation.encode("utf-8"), j.encode("utf-8")])
                                continue

                            # 如果关系中有字在问句中出现则保留
                            if self.have_same_word(question_no_first_mention_words, list(relation)):
                                for j in knowledges[relation]:
                                    predicted_answer.append([i.encode("utf-8"), relation.encode("utf-8"), j.encode("utf-8")])
                                    predicted_sameword_answers.append([i.encode("utf-8"), relation.encode("utf-8"), j.encode("utf-8")])
                                continue
                                
                            # relation = relation.encode("utf-8")
                            if self.classifier.classify(question, relation.encode("utf-8"), mention[0]):
                            # if self.classifier.classify(question, relation.encode("utf-8"), ""):
                                for j in knowledges[relation]:
                                    predicted_answer.append([i.encode("utf-8"), relation.encode("utf-8"), j.encode("utf-8")])

                            # 记录每个id最接近的relation
                            similarity = self.question_relation_similar(question, relation.encode("utf-8"), mentions[0])
                            if similarity > max_similar:
                                max_similar = similarity
                                predict_similar_answer = [i.encode("utf-8"), relation.encode("utf-8"), knowledges[relation][0].encode("utf-8")]


                        if predicted_answer:
                            predicted_answers.append(predicted_answer)

                        # if predicted_sameword_answer:
                        #     predicted_sameword_answers.append(predicted_sameword_answer)

                        if predict_similar_answer:
                            predict_similar_answers.append(predict_similar_answer)
                # if "大花组是什么科的植物" in question:
                #     print "predicted_sameword_answers ", len(predicted_sameword_answers)
                #     print "predict_similar_answers ", len(predict_similar_answers)
                #     print "predicted_answers ", len(predicted_answers)
                #     print "relation_names ", len(relation_names)
                    # print predicted_sameword_answers[0][0]
                    # print predicted_sameword_answers[0][1]
                    # print predicted_sameword_answers[0][2]
                w.write("-----------------------------------\n")
                w.write(question + "\t" + answer + "\n")

                have_answer = False
                # 保留关系和问句中有相同字的三元组
                if (not relation_names) and (predicted_sameword_answers):
                    for predicted_sameword_answer in predicted_sameword_answers:
                        if predicted_sameword_answer[1] == predicted_sameword_answer[2]:
                            continue
                        for j in predicted_sameword_answer:
                            w.write(j + "\t")
                            have_answer = True
                        w.write("\n")
                    if have_answer:
                        continue

                for i in predicted_answers:
                    # 如果三元组中id和relation相同则丢弃该结果
                    for predicted_answer in i:
                        if predicted_answer[0] == predicted_answer[1]:
                            continue

                        # 如果某个三元组关系出现在问句中
                        # 则任何三元组关系没有出现在这些关系中的三元组被丢弃
                        if relation_names:
                            if predicted_answer[1] not in relation_names:
                                continue
                        for j in predicted_answer:
                            w.write(j + "\t")
                            have_answer = True
                        w.write("\n")

                if not have_answer:
                    if not predict_similar_answers:
                        print "no similar answer"
                    for i in predict_similar_answers:
                        for j in i:
                            w.write(j + "\t")
                        w.write("\n")

        print "Done run"


if __name__ == "__main__":
    word_vector_file = "/users1/ymli/wlj/wordvector/sogou_100_nobinary"
    focus_file = "../results/focus/focus.txt"
    paraphrase_file = "../corpus/paraphrase/mergeallresult.txt"
    doubt_words_file = "../rule/questionwords.txt"
    # model_file = "sigmoid_svm_nopara_model.txt"
    # model_file = "./model/svm_embedding_model.txt"
    # model_file = "./model/svm_sogou_removedoubt_model.txt"
    model_file = "./model/svm_sogou_newtrain.model"

    classifier = Classifier(model_file, word_vector_file, focus_file, paraphrase_file, doubt_words_file)


    name2idpath = "../corpus/nlpcc-iccpol-2016.kbqa.kb.mention2id"
    triplepath = "../corpus/nlpcc-iccpol-2016.kbqa.kb"
    question2idfile = "../results/matchentity/test_filter_by_ner_count.txt"
    answer_file = "./results/predicted_answers_svm_rule_newtrain2.txt"

    cla = ClassifyResult(classifier, name2idpath, triplepath, question2idfile, answer_file)
    cla.run()
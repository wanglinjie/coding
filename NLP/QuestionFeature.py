#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160503
Last Modified: 
通过句法分析获取问句特征
'''

# from data.TrainData import TrainData
from utils.Parse import Parsing
# from utils.Data import Data

class QuestionFeature(object):
    def __init__(self, lexicon_path=""):
            self._parse = Parsing(lexicon_path)

            self.save_postags = ["nh", "ns", "nz", "ni", "nd", "i", "v", "ws", "q", "j", "r", "k", "n"]

    def parse(self, sentence, entrys):
        '''
        对句子进行依存句法解析
        '''
        words = []
        # for i, j in enumerate(sentence):
        for j in sentence:
            # if i == 1:
            #     words.append(j)
            #     continue
            # 保证实体不被切分
            if j in entrys:
                words.append(j)
                continue

            word = self._parse.segment(j)
            words.extend(word)
        # words = self._parse.segment(sentence)
        try:
            postags = self._parse.postag(words)
        except:
            for i in words:
                print i
            assert(1==2)
        # arcs = self._parse.parse(words, postags)
        # netags = self._parse.recognize(words, postags)
        # return words, postags, arcs, netags
        return words, postags


    def get_question_label(self, question):
        '''
        获取问题类别：选择、特指
        '''
        # choice_keyword = ["还是", "是不是"]
        if "还是" in question:
            return 2
        elif "是不是" in question:
            return 3
        else:
            # 特指问句
            return 1

    def get_what_feature(self, question, entitynames):
        '''
        获取特指问句的特征
        实体使用对应词性表示
        问句中确保不被切分的实体知识抽取候选实体中第一个
        '''
        features = []
        # words, postags, arcs, netags = self.parse(question, entitynames)
        words, postags = self.parse(question, entitynames)
        for entityname in entitynames:
            if entityname in words:
                entity_position = words.index(entityname)
                features.append(postags[entity_position])
        for position, postag in enumerate(postags):
            if (postag in self.save_postags) and (words[position] not in entitynames):
                features.append(words[position])
        return features


    def get_question_feature(self, question, entitynames):
        '''
        sentence是需要解析的问句
        entityname是问句中匹配的实体，需要是经过挑选的
        '''
        # 实体、实体修饰的内容、动词、head节点
        # 疑问词、疑问词修饰的内容
        # features = {}
        features = []
        entrys = []

        question_label = self.get_question_label(question)
        for entityname in entitynames:
            question = question.replace(entityname, " " + entityname + " ")
            entrys.append(entityname)


        if question_label == 1:
            # question = question.split()
            features = []
            # 处理特指问句
            # features = self.get_what_feature(question, entrys)
            # entity_position = words.index(entityname)
            # features.append(postags[entity_position])
        else:
            if question_label == 2:
                question = question.replace("还是", " 还是 ").split()
                entrys.append("还是")
            else:
                # 处理"是不是"型问句
                question = question.replace("是不是", " 是不是 ").split()
                entrys.append("是不是")

            # words, postags, arcs, netags = self.parse(question, entrys)
            words, postags = self.parse(question, entrys)

            if question_label == 2:
                # 选取还是前后的非助动词
                keyword_position = words.index("还是")
                left_position = keyword_position - 1
                num = 0
                while left_position >= 0:
                    if postags[left_position] != "u":
                        num += 1
                        features.append(words[left_position])
                    left_position -= 1
                    if num > 1:
                        break
                right_position = keyword_position + 1
                num = 0
                while right_position < len(postags):
                    if postags[right_position] != "u":
                        num += 1
                        features.append(words[right_position])
                    right_position += 1
                    if num > 1:
                        break
            else:
                # 选取是不是后面非助动词、介词、符号
                removepos = ["u", "wp", "d", "p"]
                keyword_position = words.index("是不是")
                if (keyword_position + 1) < len(postags):
                    for i in xrange(keyword_position + 1, len(postags)):
                        if postags[i] not in removepos:
                            features.append(words[i])
                else:
                    print "是不是 error"

        return "".join(features), question_label

def get_features():
    features_file = "./results/features.txt"
    result_file = "./results/bag_features.txt"
    features = {}
    with open(features_file, "r") as r:
        num = 0
        for line in r:
            if line.startswith("------"):
                continue
            num += 1
            num %= 3
            if not num:
                line_split = line.strip().split("\t")
                for feature in line_split:
                    if feature not in features:
                        features[feature] = True
    with open(result_file, "w") as w:
        for feature in features:
            w.write(feature + "\n")
    print len(features)



def get_train_feature():
    ques_feature = QuestionFeature()

    # question_mention_file = "./results/filter_by_ner_count.txt"
    question_mention_file = "./results/relation/wrong_train_relations.txt"
    feature_file = "./results/train_data/wrong_train_relation_features.txt"
    # feature_file = "./results/features.txt"
    with open(question_mention_file, "r") as r, open(feature_file, "w") as w:
        num = 0
        for line in r:
            if line.startswith("------"):
                w.write(line)
                continue
            num += 1
            num %= 2
            if num:
                line_split = line.strip().split("\t")
                if len(line_split) < 3:
                    print line, "less than 3 content"
                    continue
                question = line_split[0]
                answer = line_split[1]
                mentions = line_split[2:]
                question_words = question.strip("？")
                question_words = question.replace(mentions[0], "")
                # print question
                features, question_label = ques_feature.get_question_feature(question, mentions[0:1])

                w.write(line)
                w.write(str(question_label) + "\n")
                for i in features:
                    w.write(i + "\t")
                w.write("\n")
            else:
                w.write(line)
                # w.write("----------------------------\n")


def feature_data():
    '''
    问句特征词袋以及三元组中关系词袋
    获取训练数据中的one-hot表示
    '''
    _parse = Parsing()

    question_features = []
    triple_features = []

    question_feature_file = "./results/bag_features.txt"
    triple_feature_file = "./preprocess/results/train_relation_words.txt"

    rfile = "./results/train_data/wrong_train_relation_features.txt"
    wfile = "./results/train_data/wrong_train_data_one_hot.txt"

    with open(question_feature_file, "r") as r:
        for line in r:
            word = line.strip()
            question_features.append(word)
    with open(triple_feature_file, "r") as r:
        for line in r:
            word = line.strip()
            triple_features.append(word)

    question_features_len = len(question_features)
    triple_features_len = len(triple_features)

    with open(rfile, "r") as r, open(wfile, "w") as w:
        num = 0
        features = [0] * (question_features_len + triple_features_len)
        for line in  r:
            if line.startswith("--"):
                continue
            
            
            num += 1
            num %= 4
            # line_split = line.strip().split("\t")
            if num == 3:
                question_words = line.strip().split("\t")
                for i in question_words:
                    if i in question_features:
                        word_index = question_features.index(i)
                        features[word_index] = 1
                        # print word_index
                    else:
                        print i, "not in question features"
                # print len(question_words), "q"
            elif num == 0:
                if not line.strip():
                    features = [0] * (question_features_len + triple_features_len)
                    continue
                line_split = line.strip().split("\t")
                
                for relation in line_split:
                    relation_word = _parse.segment(relation)
                    for i in relation_word:
                        if i in triple_features:
                            relation_index = triple_features.index(i)
                            features[question_features_len+relation_index] = 1
                        # else:
                            # print i, "not in relation features"
                    # print len(relation_word), "r"
                for i in features[0:-1]:
                    w.write(str(i) + " ")
                w.write(str(features[-1]))
                w.write("\t" + str(0) + "\n")
                features = [0] * (question_features_len + triple_features_len)


def embedding_feature_data():
    '''
    直接将句子embedding相加获取训练数据
    '''
    _parse = Parsing()

    question_features = []
    triple_features = []

    question_feature_file = "./results/bag_features.txt"
    triple_feature_file = "./preprocess/results/train_relation_words.txt"

    rfile = "./results/train_data/wrong_train_relation_features.txt"
    wfile = "./results/train_data/wrong_train_data_one_hot.txt"

    with open(question_feature_file, "r") as r:
        for line in r:
            word = line.strip()
            question_features.append(word)
    with open(triple_feature_file, "r") as r:
        for line in r:
            word = line.strip()
            triple_features.append(word)

    question_features_len = len(question_features)
    triple_features_len = len(triple_features)

    with open(rfile, "r") as r, open(wfile, "w") as w:
        num = 0
        features = [0] * (question_features_len + triple_features_len)
        for line in  r:
            if line.startswith("--"):
                continue
            
            
            num += 1
            num %= 4
            # line_split = line.strip().split("\t")
            if num == 3:
                question_words = line.strip().split("\t")
                for i in question_words:
                    if i in question_features:
                        word_index = question_features.index(i)
                        features[word_index] = 1
                        # print word_index
                    else:
                        print i, "not in question features"
                # print len(question_words), "q"
            elif num == 0:
                if not line.strip():
                    features = [0] * (question_features_len + triple_features_len)
                    continue
                line_split = line.strip().split("\t")
                
                for relation in line_split:
                    relation_word = _parse.segment(relation)
                    for i in relation_word:
                        if i in triple_features:
                            relation_index = triple_features.index(i)
                            features[question_features_len+relation_index] = 1
                        # else:
                            # print i, "not in relation features"
                    # print len(relation_word), "r"
                for i in features[0:-1]:
                    w.write(str(i) + " ")
                w.write(str(features[-1]))
                w.write("\t" + str(0) + "\n")
                features = [0] * (question_features_len + triple_features_len)




if __name__ == "__main__":
    # get_train_feature()
    # get_features()
    feature_data()
    print "Done!"
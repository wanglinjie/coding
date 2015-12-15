#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''

@author:    Wanglj
@date:  2015.12.09
'''

import os
import copy
import threading

from nltk.parse import stanford

os.environ['STANFORD_PARSER'] = '/data/stanfordnlp/stanford-parser-full-2015-01-30/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/data/stanfordnlp/stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models.jar'

java_path = "/opt/jdk1.8.0_45/bin"
os.environ['JAVA_HOME'] = java_path

class SyntaxTree(threading.Thread):
    '''
    获得句子的语法树结构
    '''
    def __init__(self, readfile, writefile, start, end,  threadName):
        super(SyntaxTree, self).__init__(name = threadName)

        self.start_num = start
        self.end_num = end

        self.readfile = readfile
        self.writefile = writefile
        self.parser = stanford.StanfordParser(model_path="/data/stanfordnlp/stanford-parser-full-2015-01-30/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")


    def get_tree(self, list_sentence, words):
        '''
        获得这个句子中词的结合顺序
        '''
        # print list1
        # print words
        list1 = copy.deepcopy(list_sentence)
        words_num = len(words)

        # 去除词两侧的括号之后，两个词是否相邻

        while list1[0] == "(":
            del_num = []
            for i in xrange(len(list1)):
                if list1[i] not in "()":
                    num = 1
                    # print i
                    # print list1
                    while (list1[i-num] in "(") and (list1[i+num] in ")"):
                        del_num.append(i-num)
                        del_num.append(i+num)
                        num = num + 1
                        # print num
                    # if num == 1:
                    #     if list1[i-1] in "(":
                    #         del_num.append(i-1)
                    #     if (i+1 < len(list1)) and (list1[i+1] in ")"):
                    #         del_num.append(i+1)

        
            del_num = list(set(del_num))
            # del_num.reverse()
            del_num = sorted(del_num)
            del_num.reverse()
            
            # print del_num
            # print list1
            for i in del_num:
                # print i
                # print del_num
                del list1[i]


            list1_num = len(list1)
            for i in xrange(list1_num):
                if i < len(list1):
                    if list1[i] not in "()":
                        while (i + 1 < len(list1)) and (list1[i+1] not in "()"):
                            index1 = words.index(list1[i])
                            index2 = words.index(list1[i+1])
                            list1[i] = str(index1) + ',' + str(index2)
                        
                            words.append(list1[i])
                            del list1[i+1]

                else:
                    break
        # print words[words_num:]
        return words[words_num:]


    def run(self):
        '''
        从文件中读取句子并通过语法解析器获得句子中词的结合顺序
        '''
        with open(self.readfile, 'r') as r, open(self.writefile, 'w') as w:
            num = 0
            # print self.getName()
            # print self.end_num
            # print self.start_num
            for line in r:

                num = num + 1
                if num < self.start_num:
                    continue
                if num > self.end_num:
                    break
                
                try:
                    sentences = self.parser.raw_parse_sents((line,))
                except:
                    print "parser error ", line
                for sentence in sentences:
                    # print sentences
                    # 每个字符是一项，英文词被分割成字母组成
                    list1 = list(str(sentence))

                    # print list1

                    # 去除语法标注信息和空格
                    word_list = []
                    for i in list1:
                        if i in "( ":
                            while (len(word_list)>=1) and (word_list[-1] not in ')('):
                                word_list.pop()
                        if i != " ":
                            word_list.append(i)
                    # print word_list

                    list1 = []
                    # 记录分词之后的每个词
                    words = []
                    for i in word_list:
                        if i == ")":
                            word = ''
                            while list1[-1] not in "()":
                                # 将一个英文词各个字母联合组成词
                                j = list1.pop()
                                word = j + word
                            if word:
                                list1.append(word)
                                words.append(word)
                        list1.append(i)
                    # print list1
                    # print words
                    order = self.get_tree(list1, words)
                    #写入文件
                    string1 = ""
                    for i in order:
                        string1 = string1 + i + " "
                    # print string1
                    try:
                        w.write(string1 + '\n')
                        w.flush()
                    except:
                        print "except ", string1
                    # print string1
                    # w.flush()
        print self.getName(), "done"


if __name__ == "__main__":
    readfile = "/users1/ymli/wlj/paraphrase/test2/en_giga_seg_show_piece_5"
    writefile_ori = "/users1/ymli/wlj/dataset/syntree_piece_5"
    total_line = 500000
    thread_num = 5
    handle_num = int(total_line / thread_num)
    threads = []
    for i in range(thread_num):
        start = i * handle_num + 1
        end = start + handle_num - 1
        if i == thread_num - 1:
            end = total_line

        writefile = writefile_ori + '_' + str(i) + '.txt'
        syn = SyntaxTree(readfile, writefile, start, end, 'thread-' + str(i))
        threads.append(syn)
        # syntree.get_synsyntax()
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print "end in the main thread!"

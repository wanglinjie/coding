#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160427
Last Modified: 
Trie构造以及查找
'''

import gc

class TokenTrieNode(object):
    '''
    Trie树中节点信息
    '''
    def __init__(self, token):
        self.value = token
        self.IsEnd = False
        self.parent = None
        # self.mentionidlist = []
        self.Children = {}

    def contains(self, token):
        '''
        判断当前节点的孩子中是否有token
        '''
        return self.Children.has_key(token)

    def getchild(self, token):
        '''
        获取当前节点的孩子节点，边为token
        '''
        if token in self.Children:
            return self.Children[token]
        else:
            return None

class TokenTrie(object):
    '''
    Trie树
    '''
    def __init__(self):
        self.rootNode = TokenTrieNode("_$ROOT$_")

    def getroot(self):
        '''
        获取root节点
        '''
        return self.rootNode

    # def inserts(self, tokens, mentionid):
    def inserts(self, tokens):
        '''
        往Trie树中添加词条
        '''
        if not tokens:
            return None
        node = self.rootNode
        for token in tokens:
            parent = node
            node = self.insert(token, node)
            node.parent = parent
        node.IsEnd = True
        # if mentionid not in node.mentionidlist:
        #     node.mentionidlist.append(mentionid)


    def insert(self, token, node):
        '''
        往Trie树中添加单个字节点
        '''
        # 确定传入的节点类型是TokenTrieNode
        assert(type(node) == TokenTrieNode)
        if node.contains(token):
            return node.getchild(token)
        else:
            tempNode = TokenTrieNode(token)
            node.Children[token] = tempNode
            return tempNode

class LexiconMatcher(object):
    '''
    词串匹配
    '''
    def __init__(self):
        # 实体最长长度
        self.maxEntryLength = 100
        self.tokenTrie = TokenTrie()

    def read2TrieEntity(self, filepath):
        '''
        读入实体树
        '''
        print "Loading mention names..."
        # mentionid = "_$HEAD$_"
        entryList = []  # mention2id文件中mention列表
        entityList = [] # 
        with open(filepath, "r") as r:
            for line in r:
                line_split = [i.strip() for i in line.strip().split("|||")]
                if len(line_split) != 2:
                    continue
                # mention2id文件中entry是分词之后的，包含空格，所以需要去除字符串中空格
                mention = line_split[0].replace(" ", "")
                mention = mention.lower()
                entryList.append(mention)

        for entity in entryList:
            # 使用Unicode编码，list就会按照Unicode字符来切分
            words = list(entity.decode("utf-8"))
            entityList.append(words)

        del entryList
        entryList = None
        gc.collect()

        count = 0
        entityListCount = len(entityList)
        # for tokens in entityList:
        for i in xrange(entityListCount - 1, -1, -1):
            self.tokenTrie.inserts(entityList[i])
            # self.tokenTrie.inserts(entityList[i], mentionid)
            # 及时删除不需要内容，减少内存占用空间 
            count += 1
            if (count % 100000) == 0:
                print count
                del entityList[i:]
                gc.collect()
            # if count > 200000:
            #     break
        print "Done: Loading mention names..."


    def find_tokens(self, tokens):
        '''
        查找问句中的实体
        '''
        # coll = []
        if not tokens:
            return None
        # mentionset = {}
        mentionset = []

        node = self.tokenTrie.getroot()

        count = len(tokens)
        current = 0

        while current < count:
            item = []
            # matchList = {}
            # position = current
            index = current
            token = tokens[index]
            while True:
                key = None
                if node.contains(token):
                    key = token
                else:
                    break

                node = node.getchild(key)
                item.append(key)
                if node.IsEnd:
                    # beg = current
                    # end = index
                    mention = "".join(item)
                    if mention not in mentionset:
                        # mentionset[mention] = True
                        mentionset.append(mention)


                index += 1
                if index >= count:
                    break
                token = tokens[index]

            current += 1
            node = self.tokenTrie.getroot()
        return mentionset


def main():
    # 读取训练数据
    from data.TrainData import TrainData
    # train_file = "./corpus/nlpcc-iccpol-2016.kbqa.training-data"
    polite_file = "./rule/polite.txt"

    train_file = "./data/results/train_data.txt"
    traindata = TrainData(train_file, polite_file)
    traindata.get_data()

    test_file = "./data/results/test_data.txt"
    testdata = TrainData(test_file, polite_file)
    testdata.get_data()
    # print len(traindata.train_data)
    # return

    mention2id_file = "./corpus/nlpcc-iccpol-2016.kbqa.kb.mention2id"
    lexicon = LexiconMatcher()
    lexicon.read2TrieEntity(mention2id_file)

    # string1 = "你汪尧田啊".decode("utf-8")
    # result = lexicon.find_tokens(list(string1))
    # for i in result:
    #     print i.encode("utf-8")


    with open("./results/matchentity/trainmatchentity.txt", "w") as w:
        num = 0
        for i in traindata.train_data:
            num += 1
            question = i[0].decode("utf-8")
            result = lexicon.find_tokens(list(question))
            if result:
                # w.write(i[0] + "\t" + i[1] + "\t" + result[-1].encode("utf-8") + "\n")

                w.write(i[0] + "\t" + i[1])
                for entity in result:
                    w.write("\t" + entity.encode("utf-8"))
                w.write("\n")
                print num, result[-1].encode("utf-8")
            else:
                # w.write(i[0] + "\t" + i[1] + "\n")
                print num, "no entry match"

    with open("./results/matchentity/testmatchentity.txt", "w") as w:
        num = 0
        for i in testdata.train_data:
            num += 1
            question = i[0].decode("utf-8")
            result = lexicon.find_tokens(list(question))
            if result:
                # w.write(i[0] + "\t" + i[1] + "\t" + result[-1].encode("utf-8") + "\n")

                w.write(i[0] + "\t" + i[1])
                for entity in result:
                    w.write("\t" + entity.encode("utf-8"))
                w.write("\n")
                print num, result[-1].encode("utf-8")
            else:
                # w.write(i[0] + "\t" + i[1] + "\n")
                print num, "no entry match"



if __name__ == "__main__":
    main()
    print "Done!"
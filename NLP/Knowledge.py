#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160503
Last Modified: 
存储知识库知识，并查找
'''

class Knowledge(object):
    def __init__(self, name2idpath, triplepath):
        self.name2idpath = name2idpath
        self.entity2idDict = {}

        # 知识库文件路径
        self.triplepath = triplepath
        self.tripleDict = {}

    def load_name2id(self):
        '''
        加载实体转换
        '''
        print "Loading mention-to-id file..."
        with open(self.name2idpath, "r") as r:
             for line in r:
                line_split = [i.strip() for i in line.strip().lower().split("|||")]
                if len(line_split) != 2:
                    continue
                mention = line_split[0].replace(" ", "").decode("utf-8")
                ids = [i.strip().decode("utf-8") for i in line_split[1].split("\t")]
                if mention not in self.entity2idDict:
                    self.entity2idDict[mention] = []

                for i in ids:
                    if i not in self.entity2idDict[mention]:
                        self.entity2idDict[mention].append(i)
        print "Done: Loading mention-to-id file"

    def load_triple(self):
        '''
        加载知识库中三元组
        '''
        removeSymbol = [u"•", u"-", u"【", u"】", u"啊"]
        print "Loading triple file..."
        with open(self.triplepath, "r") as r:
            for line in r:
                line_split = [i.strip().decode("utf-8") for i in line.strip().lower().split("|||")]
                if len(line_split) != 3:
                    continue
                kbsubject = line_split[0]
                relation = line_split[1]
                for i in removeSymbol:
                    relation = relation.strip(i)
                relation = relation.replace(" ", "")
                if not relation:
                    relation = "-"
                    # continue

                kbobject = line_split[2]

                if kbsubject not in self.tripleDict:
                    self.tripleDict[kbsubject] = {}
                if relation not in self.tripleDict[kbsubject]:
                    self.tripleDict[kbsubject][relation] = []
                if kbobject not in self.tripleDict[kbsubject][relation]:
                    self.tripleDict[kbsubject][relation].append(kbobject)
        print "Done: Loading triple file"

    def GetEntityIdByName(self, entityName):
        '''
        通过问句实体获取知识库中实体
        '''
        if not entityName:
            return []

        result = []
        if entityName in self.entity2idDict:
            result = self.entity2idDict[entityName]
        return result
        

    def GetPredicatesByEntityId(self, entityID):
        '''
        通过知识库中实体获取知识
        '''
        if not entityID:
            return {}

        result = {}
        if entityID in self.tripleDict:
            result = self.tripleDict[entityID]
        return result

    
    def GetValuesByEntityPredicate(self, entityID, predicate):
        '''
        通过知识内容获取知识中的值
        '''
        if (not entityID) or (not predicate):
            return []

        result = []
        if (entityID in self.tripleDict) and (predicate in self.tripleDict[entityID]):
            result = self.tripleDict[entityID][predicate]
        return result

    def GetRelation(self, entityID, answer):
        '''
        根据实体ID和答案获取关系
        '''
        if (not entityID) or (not answer):
            return []

        result = set()
        if entityID in self.tripleDict:
            value = self.tripleDict[entityID]
            for relation in value:
                if answer in value[relation]:
                    result.add(relation)
        return list(result)

    def GetWrongRelation(self, entityID, answer):
        '''
        根据实体ID和答案获取关系
        '''
        if (not entityID) or (not answer):
            return []

        result = set()
        if entityID in self.tripleDict:
            value = self.tripleDict[entityID]
            for relation in value:
                if answer not in value[relation]:
                    result.add(relation)
        return list(result)


def main():
    pass


if __name__ == "__main__":
    main()
    print "Done!"
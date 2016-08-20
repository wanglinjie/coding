#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160820
from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre_dic = defaultdict(set)
        rely_dic = defaultdict(set)
        points = set()
        for i in xrange(numCourses):
            points.add(i)
        for i in prerequisites:
            pre_dic[i[0]].add(i[1])
            rely_dic[i[1]].add(i[0])
        if len(pre_dic) == numCourses:
            return []
        ret = []
        ret = self.findpath(pre_dic, rely_dic, points)
        return ret

    
    def findpath(self, pre_dic, rely_dic, points):
        ret = []
        no_pre = []
        for i in points:
            if i not in pre_dic:
                no_pre.append(i)
        if not no_pre:
            return ret
        for i in no_pre:
            points.remove(i)
            for j in rely_dic[i]:
                pre_dic[j].remove(i)
                if not pre_dic[j]:
                    del pre_dic[j]
        if not points:
            return no_pre

        result = self.findpath(pre_dic, rely_dic, points)
        if not result:
            return []
        ret = no_pre + result
        return ret



n = 4
pre = [[0,1],[3,1],[1,3],[3,2]]
so = Solution()
print so.findOrder(n, pre)
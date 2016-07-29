#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160729

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
        """
        ret = [1]
        for i in xrange(1, rowIndex+1):
            temp = []
            for j in xrange(i+1):
                if j:
                    if j < i:
                        temp.append(ret[j-1] + ret[j])
                    else:
                        temp.append(ret[j-1])
                else:
                    temp.append(ret[j])
            ret = temp
        return ret
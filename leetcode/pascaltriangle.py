#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160729

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
        """
        if not numRows:
            return []
        ret = [[1]]
        for i in xrange(1, numRows):
            temp = []
            for j in xrange(i+1):
                if j:
                    if j < i:
                        temp.append(ret[-1][j-1]+ret[-1][j])
                    else:
                        temp.append(ret[-1][j-1])
                else:
                    temp.append(ret[-1][j])
            ret.append(temp)
        return ret

numRows = 4
so = Solution()
print so.generate(numRows)
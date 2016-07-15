#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160714

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

Given two words word1 and word2, 
find the minimum number of steps required to convert word1 to word2. 
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character 
b) Delete a character
c) Replace a character
        """
        word1_len = len(word1)
        word2_len = len(word2)
        m = word1_len + 1
        n = word2_len + 1
        # if not word1_len:
        #     return word2_len
        # elif not word2_len:
        #     word1_len
        matrix = [[0] * n for i in xrange(m)]
        for i in xrange(n):
            # 第一行初始化为0, 1, 2 ...
            matrix[0][i] = i
        for i in xrange(m):
            # 第一列初始化为0, 1, 2 ...
            matrix[i][0] = i
        for i in xrange(1, m):
            for j in xrange(1, n):
                temp = 0
                if word1[i-1] != word2[j-1]:
                    # 如果word1中第i-1为和word2中第j-1为不相等，则temp为1
                    temp = 1
                # 当前位置数值为左侧+1，右侧+1以及左上方+temp中三个值的最小值
                matrix[i][j] = min(min(matrix[i][j-1] + 1, matrix[i-1][j] + 1), matrix[i-1][j-1] + temp)
                # print i, j, matrix[i][j]

        return matrix[m-1][n-1]
        # print matrix


word1 = "hello"
word2 = ""
so = Solution()
print so.minDistance(word1, word2)
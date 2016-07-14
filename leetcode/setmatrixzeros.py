#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160713
import sys
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

思路：
为了避免一开始就将0所在行以及所在列元素置0，导致后续被置0元素的所在行和所在列也被置0
将需要被置0的元素置为sys.maxint
第二次遍历将元素值为sys.maxint的元素置为0
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        # 先将0所在行以及所在列元素置为sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if not matrix[i][j]:
                    for temp in xrange(n):
                        if matrix[i][temp]:
                            matrix[i][temp] = sys.maxint
                    for temp in xrange(m):
                        if matrix[temp][j]:
                            matrix[temp][j] = sys.maxint
        # 二次遍历，将矩阵中值为sys.maxint的元素置为0
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == sys.maxint:
                    matrix[i][j] = 0

matrix = [[4, 0, 6]]
so = Solution()
so.setZeroes(matrix)
print matrix
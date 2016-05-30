#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

动态规划
        """
        if (n <= 0) or (m <= 0):
            return 0
        path_num = [[0] * n] * m
        # path_num[0][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                upper = 0
                left = 0
                if i > 0:
                    upper = path_num[i-1][j]
                if j > 0:
                    left = path_num[i][j-1]
                path_num[i][j] = max(upper + left, 1)
        return path_num[m-1][n-1]

so = Solution()
print so.uniquePaths(4, 5)
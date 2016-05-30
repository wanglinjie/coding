#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int


Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
        """
        if not obstacleGrid:
            return 0
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        path_num = [[0] * columns] * rows

        for i in xrange(rows):
            for j in xrange(columns):
                if obstacleGrid[i][j] == 1:
                    path_num[i][j] = 0
                    continue
                if (i == 0) and (j == 0):
                    path_num[i][j] = 1
                    continue
                upper = 0
                left = 0
                if i > 0:
                    upper = path_num[i - 1][j]
                if j > 0:
                    left = path_num[i][j - 1]
                path_num[i][j] = upper + left
        return path_num[rows-1][columns-1]


A = [ [0,0,0], [1,1,1], [0,0,0]]
# A = [[1]]
so = Solution()
print so.uniquePathsWithObstacles(A)

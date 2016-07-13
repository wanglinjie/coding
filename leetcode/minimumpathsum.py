#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160712

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

思路：
动态规划思想
使用一个新的矩阵存储到当前位置的最短路径
        """
        m = len(grid)
        n = len(grid[0])
        paths = []
        for i in xrange(m):
            paths.append([0] * n)
        for i in xrange(m):
            for j in xrange(n):
                if i:
                    if j:
                        # 当前位置左边和上边较小值和当前位置数字相加
                        paths[i][j] = grid[i][j] + min(paths[i-1][j], paths[i][j-1])
                    else:
                        # 在矩阵最左侧，只能从上面元素到当前位置
                        paths[i][j] = grid[i][j] + paths[i-1][j]
                else:
                    if j:
                        paths[i][j] = grid[i][j] + paths[i][j-1]
                    else:
                        paths[i][j] = grid[i][j]
        print paths
        return paths[m-1][n-1]

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
so = Solution()
print so.minPathSum(grid)
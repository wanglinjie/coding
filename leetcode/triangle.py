#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160620

import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int


Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).


动态规划，记录到达当前位置最小值
可以到达当前位置的是上层相邻位置
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        triangle_len = len(triangle)
        for x in xrange(1, triangle_len):
            line_len = len(triangle[x])
            for y in xrange(line_len):

                if y:
                    if y >= len(triangle[x-1]):
                        # 如果当前位置比上层个数多，则只计算当前位置上层左侧元素
                        triangle[x][y] = triangle[x-1][y-1] + triangle[x][y]
                    else:
                        triangle[x][y] = min(triangle[x-1][y-1], triangle[x-1][y]) + triangle[x][y]
                else:
                    # 如果当前是列表第一个元素，则只需计算上层第一个元素
                    triangle[x][y] = triangle[x-1][y] + triangle[x][y]
        return min(triangle[-1])

triangle = [[1],[1,4],[6,1,7],[1,6,8,3]]
so = Solution()
print so.minimumTotal(triangle)
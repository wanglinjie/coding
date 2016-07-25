#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160724

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] = heights[j] + 1
            max_area = max(max_area, self.largestRectangle(heights, n))
        return max_area
    
    def largestRectangle(self, heights, n):
        max_left = [0] * n
        max_right = [0] * n
        max_area = 0
        for i in xrange(n):
            left = i - 1
            while (left >= 0) and (heights[left] >= heights[i]):
                left = max_left[left]
            max_left[i] = left
        for i in xrange(n-1, -1, -1):
            right = i + 1
            while (right < n) and (heights[right] >= heights[i]):
                right = max_right[right]
            max_right[i] = right
        for i in xrange(n):
            area = heights[i] * (max_right[i] - max_left[i] - 1)
            if area > max_area:
                max_area = area
        return max_area

matrix = ["10100","10111","11111","10010"]
so = Solution()
print so.maximalRectangle(matrix)
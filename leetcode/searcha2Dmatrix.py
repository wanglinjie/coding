#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160714

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m-1
        # 注意在二分查找中最好使用low<=high作为判断条件
        # 这样可以避免low或者high指向的位置元素就是所希望查找的元素
        while low <= high:
            mid = low + (high - low) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        line = low
        # print line
        while (line >= m) or (matrix[line][0] > target):
            line -= 1
            if line < 0:
                return False
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) / 2
            if matrix[line][mid] == target:
                return True
            elif matrix[line][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 12
matrix = [[1]]
target = 0
# matrix = [[1],[3]]
# target = 3
so = Solution()
print so.searchMatrix(matrix, target)
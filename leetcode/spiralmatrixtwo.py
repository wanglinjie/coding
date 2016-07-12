#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160711

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
        """
        if not n:
            return []
        rows = n
        columns = n
        loop = 0
        if n & 0x1:
            loop = n / 2 + 1
        else:
            loop = n / 2
        # 为什么使用下面创建数组，matrix[1][2]=1赋值，会将第2列的值都赋值为1？
        # matrix = [[0] * n] * n
        matrix = []
        for i in xrange(n):
            matrix.append([0] * n)
        number = 1
        for i in xrange(loop):
            row = i
            column = i

            read_num = 0
            read_rows = rows - 2 * i
            read_columns = columns - 2 * i
            if (read_rows == 1) or (read_columns == 1):
                read_num = read_rows * read_columns
            else:
                read_num = 2 * read_rows + 2 * (read_columns - 2)
            while read_num:
                read_num -= 1
                matrix[row][column] = number
                # print matrix
                # print row, column, number
                # print 
                number += 1
                if (row == i) and (column < (columns - i - 1)):
                    column += 1
                elif (column == (columns - i - 1)) and (row < (rows - i - 1)):
                    row += 1
                elif (row == (rows - i - 1)) and (column > i):
                    column -= 1
                elif (column == i) and (row > i):
                    row -= 1
        return matrix
n = 3
# so = Solution()
# print so.generateMatrix(n)
matrix = [[0] * n] * n
# matrix = []
# for i in xrange(n):
#     matrix.append([0]*n)
# matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print matrix
matrix[0][1] = 1
print matrix
print matrix[0][2]
matrix[0][2] = 2
print matrix
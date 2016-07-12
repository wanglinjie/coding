#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160711

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

思路：
从对角线元素开始遍历，遍历一圈
        """
        if not matrix:
            return []

        # 获取矩阵行数
        rows_num = len(matrix)
        # 获取矩阵列数
        columns_num = len(matrix[0])
        if not columns_num:
            return []

        # 记录螺旋后结果
        ret = []
        # 记录矩阵需要遍历几圈
        loop = 0
        min_rows_columns = min(rows_num, columns_num)
        if min_rows_columns & 0x1:
            # 如果矩阵行列数最小值为奇数
            loop = min_rows_columns / 2 + 1
        else:
            # 如果矩阵行列数最小值为偶数
            loop = min_rows_columns / 2
        for i in xrange(loop):
            # 该圈遍历起始位置
            row = i
            column = i

            # 记录该次遍历需要读取元素个数
            read_num = 0
            read_row = rows_num - 2 * i
            read_column = columns_num - 2 * i
            if (read_row == 1) or (read_column == 1):
                read_num = read_row * read_column
            else:
                read_num = 2 * read_row + 2 * (read_column - 2)
            while read_num:
                read_num -= 1
                # 添加这个元素
                ret.append(matrix[row][column])
                if (row == i) and (column < (columns_num - i - 1)):
                    # 在一圈中，读取方向向右移
                    column += 1
                elif (column == (columns_num - i - 1)) and (row < (rows_num - i - 1)):
                    # 在一圈中，读取方向向下移
                    row += 1
                elif (row == (rows_num - i - 1)) and (column > i):
                    # 在一圈中，读取方向向左移
                    column -= 1
                elif (column == i) and (row > i):
                    # # 在一圈中，读取方向向上移
                    row -= 1
        return ret


matrix = [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ],
    [10, 11, 12]
    ]
so = Solution()
print so.spiralOrder(matrix)
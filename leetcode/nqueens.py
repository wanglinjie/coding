#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160723

import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

The n-queens puzzle is the problem of placing n queens on an 
n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

同行：行坐标相同，或者行坐标相减为0
同列：列坐标相同，或者列表做相减为0
在对角线上：行坐标相减绝对值等于列坐标相减绝对值
        """
        ret = []
        queens = []
        for i in xrange(n):
            queens.append(['.'] * n)
        flag_col = [1] * n
        flag_45 = [1] * (2 * n -1)
        flag_135 = [1] * (2 * n -1)
        self.recursiveSolveNQueens(ret, queens, flag_col, flag_45, flag_135, 0, n)
        return ret

    def recursiveSolveNQueens(self, ret, queens, flag_col, flag_45, flag_135, row, n):
        if row == n:
            new_queens = ["".join(i) for i in queens]
            ret.append(new_queens)
            return
        for i in xrange(n):
            if flag_col[i] and flag_45[row+i] and flag_135[n-1+i-row]:
                flag_col[i] = flag_45[row+i] = flag_135[n-1+i-row] = 0
                queens[row][i] = "Q"
                self.recursiveSolveNQueens(ret, queens, flag_col, flag_45, flag_135, row+1, n)
                queens[row][i] = "."
                flag_col[i] = flag_45[row+i] = flag_135[n-1+i-row] = 1


n = 5
so = Solution()
print so.solveNQueens(n)
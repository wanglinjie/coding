#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160801

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.

Given a 2D board containing 'X' and 'O' (the letter O), 
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


广度优先搜索，判断从当前位置的O是否可以进入到矩阵的四周

使用set存储已经遍历的节点
        """
        if not board or len(board) < 2 or len(board[0]) < 2:
            return
        m, n = len(board), len(board[0])
        
        for i in xrange(m):
            if board[i][0] == 'O' : self.dfs(board, i, 0)
            if board[i][n-1] == 'O': self.dfs(board, i, n-1)
        for j in xrange(n):
            if board[0][j] == 'O': self.dfs(board, 0, j)
            if board[m-1][j] == 'O': self.dfs(board, m-1, j)
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '*': board[i][j] = 'O'
        
    def dfs(self, board, i, j):
        if board[i][j] != 'O': 
            return
        board[i][j] = '*'
        if i > 1:
            self.dfs(board, i-1, j)
        if j > 1:
            self.dfs(board, i, j-1)
        if i < len(board) - 2:
            self.dfs(board, i+1, j)
        if j < len(board[0]) - 2:
            self.dfs(board, i, j+1)


# board = [["X", "X", "X", "X"], 
# ["X", "O", "O", "X"],
# ["X", "X", "O", "X"],
# ["X", "O", "X", "X"]]
# board = ["XOXOXOOOXO","XOOXXXOOOX","OOOOOOOOXX","OOOOOOXOOX","OOXXOXXOOO","XOOXXXOXXO","XOXOOXXOXO","XXOXXOXOOX","OOOOXOXOXO","XXOXXXXOOO"]
# # board = ["XOXOXOOOXO","XOOXXXOOOX","OOOOOOOOXX","OOOOOOXOOX","OOXXOXXOOO","XOOXXXXXXO","XOXXXXXOXO","XXOXXXXOOX","OOOOXXXOXO","XXOXXXXOOO"]
board = ["XOOXXXOXXOOOOOOOOOOO","XOOXXOOXOOOXOXOXOOXO","OOOXXXXOXOXXOOOOXOXO","OOOXXOOXOOOXXXOOXOOX","OOOOOOOXXXOOOOOOOOOO","XOOOOXOXOXXOOOOOOXOX","OOOXOOOXOXOXOXOXOXOX","OOOXOXOOXXOXOXXOXXXO","OOOOXOOXXOOOOXOOOXOX","OOXOOXOOOOOXOOXOOOXO","XOOXOOOOOOOXOOXOXOXO","OXOOOXOXOXXOXXXOXXOO","XXOXOOOOXOOOOOOXOOOX","OXOOXXXOOOXXXXXOXOOO","OOXXXOOOXXOOOXOXOOOO","XOOXOXOOOOXOOOXOXOXX","XOXOOOOOOXOOOXOXOOOO","OXXOOOXXXOXOXOXXXXOO","OXOOOOXXOOXOXOOXOOXX","OOOOOOXXXXOXOOOXXOOO"]
for i in xrange(len(board)):
    board[i] = list(board[i])
print board
so = Solution()
so.solve(board)
print board
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160723

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool


Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
        """
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if self.recursiveExist(board, i, j, word, 0):
                    return True
        return False

    def recursiveExist(self, board, x, y, word, position):
        if position == len(word):
            return True

        if (y<0) or (x<0) or (x==len(board)) or (y==len(board[0])):
            return False

        if board[x][y] != word[position]:
            return False

        temp = board[x][y]
        board[x][y] = "0"
        result = self.recursiveExist(board, x, y+1, word, position+1) or \
                self.recursiveExist(board, x, y-1, word, position+1) or \
                self.recursiveExist(board, x+1, y, word, position+1) or \
                self.recursiveExist(board, x-1, y, word, position+1)
        board[x][y] = temp
        return result


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCED"

so = Solution()
print so.exist(board, word)
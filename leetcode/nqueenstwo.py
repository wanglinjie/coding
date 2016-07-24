#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160723

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.


        """
        ret = 0
        tags_col = [1] * n
        tags_45 = [1] * (2 * n - 1)
        tags_135 = [1] * (2 * n - 1)
        ret = self.recursiveGetQueens(tags_col, tags_45, tags_135, 0, n)
        return ret

    def recursiveGetQueens(self, tags_col, tags_45, tags_135, row, n):
        if row == n:
            return 1
        ret = 0
        for i in xrange(n):
            if tags_col[i] and tags_45[row + i] and tags_135[n - 1 + i - row]:
                tags_col[i] = tags_45[row + i] = tags_135[n - 1 + i - row] = 0
                result = self.recursiveGetQueens(tags_col, tags_45, tags_135, row + 1, n)
                ret += result
                tags_col[i] = tags_45[row + i] = tags_135[n - 1 + i - row] = 1
        return ret

n = 3
so = Solution()
print so.totalNQueens(n)
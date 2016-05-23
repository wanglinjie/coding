#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# date:20160514

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 使用一个列表存储从2到n的每个数break后最大乘积
        # 动态规划思想
        if n <= 2:
            return 1
        max_break_list = [1] * (n + 1)
        for i in xrange(3, n+1):
            i_break_max = 1
            for j in xrange(1, i/2+1):
                break_number = max(j, max_break_list[j]) * max(i-j, max_break_list[i-j])
                if i_break_max < break_number:
                    i_break_max = break_number
            max_break_list[i] = i_break_max
        return max_break_list[n]

so = Solution()
print so.integerBreak(50)
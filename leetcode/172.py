#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160813

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
        """
        # ret = 0
        # number = 5
        # while True:
        #     if number <= n:
        #         temp = number
        #         while (temp % 5 == 0):
        #             ret += 1
        #             temp /= 5
        #     else:
        #         break
        #     number += 5
        # return ret
        r, five = 0, 5
        c = n/five
        while c>0:
            r += c
            five *= 5
            c = n/five
        return r

n = 1808548329
so = Solution()
print so.trailingZeroes(n)
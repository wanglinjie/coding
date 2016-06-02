#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int


Given an integer n, count the total number of digit 1 appearing 
in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
        """
        if n <= 0:
            return 0
        icount = 0
        ifactor = 1
        ilowernum = 0
        icurrnum = 0
        ihighernum = 0
        # 逐位判断1出现的次数
        while n / ifactor != 0:
            # 比当前位低的值大小
            ilowernum = n - (n / ifactor) * ifactor
            # 当前位上数值
            icurrnum = (n / ifactor) % 10
            # 比当前位高的数值大小
            ihighernum = n / (ifactor * 10)
            if icurrnum == 0:
                icount += ihighernum * ifactor
            elif icurrnum == 1:
                icount += ihighernum * ifactor + ilowernum + 1
            else:
                icount += (ihighernum + 1) * ifactor
            ifactor *= 10

        return icount


so = Solution()
print so.countDigitOne(99999999999)
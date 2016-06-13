#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160613

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. 
(The answer should be the total numbers in the range of 0 ≤ x < 100, 
    excluding [11,22,33,44,55,66,77,88,99])

分析：
符合条件的整数中每个位上数和其它位上不同
则可以看成10个数在1-n为位上排列
整数可以分为
当m位数中包含0
当m位数中不包含0
        """
        if n <= 1:
            return max((10 ** n), 0)
        if n > 10:
            n = 10

        ret = 1
        for i in xrange(1, n+1):
            if i == 10:
                # 如果i等于10，则整数中每个数字都必须用上
                mul_sum = 1
                for j in xrange(1, 10):
                    mul_sum *= j
                mul_sum *= 9
                ret += mul_sum
                continue

            # 整数中有0
            have_zero = 1
            for j in xrange(i-1):
                have_zero *= (9-j)
            have_zero *= (i-1)
            ret += have_zero

            # 整数中没有0
            no_zero = 1
            for j in xrange(i):
                no_zero *= (9-j)
            ret += no_zero
        return ret

so = Solution()
print so.countNumbersWithUniqueDigits(2)

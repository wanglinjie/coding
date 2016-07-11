#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160711

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str


Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
        """
        if (not num1) or (not num2):
            return 0
        int_num1 = reduce(lambda x, y: x*10 + y, [ord(i)-48 for i in num1])
        int_num2 = reduce(lambda x, y: x*10 + y, [ord(i)-48 for i in num2])
        return str(int_num1 * int_num2)

num1 = "1"
num2 = ""
so = Solution()
print so.multiply(num1, num2)
print int(num1) * int(num2)
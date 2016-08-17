#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160817

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1



思路：
按照题目意思计算下一个数字，如果下一个数字已经产生过，则证明这个数字会有一个循环过程
则不是happy number
如果为1，则是happy number
        """
        loop = 0
        read = set()
        while n != 1:
            temp = 0
            if n in read:
                return False
            else:
                read.add(n)
            while n:
                temp += (n%10)**2
                n /= 10
            n = temp
        return True

n = input("input the number:")
so = Solution()
print so.isHappy(n)
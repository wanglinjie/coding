#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160709

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

题目意思：
依次数字符串中数字，如果“1”连续出现3次（“111”），则数为“31”

思路：
从第一个一直生成到第n个
当前字符串为前一个字符串的数数
所以记录前一个字符串
        """
        if not n:
            return ""
        last = "1"

        # 生成从第一个到第n个数字
        for i in xrange(1, n):

            # 记录当前数数结果
            now = ""
            # 记录数数过程中当前数字字符
            now_num = ""
            # 记录当前字符连续出现次数
            now_num_count = 0

            # 对前一个数字进行数数
            for j in last:
                if j == now_num:
                    # 当前字符和前一个字符相同，则字符连续出现次数加1
                    now_num_count += 1
                else:
                    if now_num:
                        now += str(now_num_count) + now_num
                    # 当前字符和前一个字符不同，则更改计数对象
                    now_num = j
                    now_num_count = 1
            now += str(now_num_count) + now_num
            last = now
        return last


n = 6
so = Solution()
print so.countAndSay(n)
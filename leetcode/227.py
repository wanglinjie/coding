#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160826

import collections

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators 
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
        """
        s_len = len(s)
        operators = ["+", "-", "*", "/"]
        num_s = collections.deque()
        i = 0
        while i < s_len:
            if s[i] == " ":
                i += 1
                continue
            elif s[i] in operators:
                num_s.append(s[i])
                i += 1
            else:
                temp = 0
                while (i < s_len) and ("0" <= s[i] <= "9"):
                    temp = temp * 10 + int(s[i])
                    i += 1
                num_s.append(temp)
                self.compute(num_s)
        while len(num_s) >= 3:
            a = num_s[0]
            operator = num_s[1]
            b = num_s[2]
            num_s.popleft()
            num_s.popleft()
            if operator == "+":
                num_s[0] = a + b
            else:
                num_s[0] = a - b
        return num_s[0] if num_s else 0


    def compute(self, num_s):
        if not num_s:
            return
        if len(num_s) < 2:
            return
        operator = num_s[-2]
        if operator == "*":
            num_s[-3] = num_s[-3] * num_s[-1]
            num_s.pop()
            num_s.pop()
        elif operator == "/":
            num_s[-3] = num_s[-3] / num_s[-1]
            num_s.pop()
            num_s.pop()


s = "3 / 2"
so = Solution()
print so.calculate(s)
 
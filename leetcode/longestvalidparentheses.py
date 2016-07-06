#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160706

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int

Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", 
which has length = 4.
        """
        s_len = len(s)
        if (not s_len) or (s_len == 1):
            return 0
        input_stack = []
        stack_len = 0

        parentheses = 0
        for i in s:
            if i == "(":
                input_stack.append(i)
                stack_len += 1
            else:
                if stack_len and (input_stack[-1] == "("):
                    parentheses += 2
                    del input_stack[-1]
                    stack_len -= 1
        return parentheses
s = "())(()"
so = Solution()
print so.longestValidParentheses(s)
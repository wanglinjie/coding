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
        # 记录入栈的左括号
        input_stack = []
        # 记录入栈的左括号的位置
        input_stack_index = []
        stack_len = 0

        # 记录该位置的括号是否有成对的，有成对则为1，否则为0
        valid = [0] * s_len

        # 将成对的括号相应位标志为1
        for i in xrange(s_len):
            if s[i] == "(":
                # 如果是左括号则入栈
                input_stack.append(s[i])
                input_stack_index.append(i)
                stack_len += 1
            else:
                # 如果是右括号则判断栈中是否有左括号
                if stack_len:
                    valid[i] = 1
                    valid[input_stack_index[-1]] = 1
                    del input_stack[-1]
                    del input_stack_index[-1]
                    stack_len -= 1

        # 最长有效括号最长长度
        parentheses = 0

        temp = 0
        # 动态规划，寻找最长连续成对括号
        for i in valid:
            if i:
                temp +=1
            else:
                if parentheses < temp:
                    parentheses = temp
                temp = 0
        # 如果valid中最后一个元素为1，则这里需要再次判断最长的长度
        if temp > parentheses:
            parentheses = temp
        return parentheses
        
s = "()()()()(()()()"
so = Solution()
print so.longestValidParentheses(s)
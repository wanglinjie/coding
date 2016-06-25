#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160625

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

这个题目是求n对括号摆放的组合
我的思路是：
第一个肯定得放左括号“(”
之后递归放后续括号
如果当前剩余左括号数和右括号数相同，则只能摆放左括号
如果剩余右括号数少于左括号数，则可以摆放左括号也可以摆放右括号
递归结束条件就是没有可以摆放的左括号了，只能摆放右括号
        """
        if not n:
            return [""]
        left = n
        right = n
        ret = []
        left_gen = self.recursive_gen(left-1, right)
        for i in left_gen:
            ret.append("(" + i)
        return ret


    def recursive_gen(self, left, right):
        if not left:
            return [")" * right]
        ret = []
        left_gen = self.recursive_gen(left-1, right)
        for i in left_gen:
            ret.append("(" + i)
        if right > left:
            right_gen = self.recursive_gen(left, right-1)
            for i in right_gen:
                ret.append(")" + i)
        return ret

n = 8
so = Solution()
print so.generateParenthesis(n)
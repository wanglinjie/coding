#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160808

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

思路：
将tokens中元素入栈，判断当前元素是否为操作符，如果是操作符则将栈顶两个元素进行相应操作
        """
        if len(tokens) == 1:
            return int(tokens[0])
        operators = set(["+", "-", "*", "/"])
        s = []
        num = 0
        for i in tokens:
            if i in operators:
                a = s[-2]
                b = s[-1]
                if i == "+":
                    num = a + b
                elif i == "-":
                    num = a - b
                elif i == "*":
                    num = a * b
                else:
                    # 注意此处，如果是a/b，则10/-120=-1，而正确结果应该是0
                    num = int(operator.truediv(a, b))
                del s[-1]
                del s[-1]
                s.append(num)
            else:
                s.append(int(i))
        return num
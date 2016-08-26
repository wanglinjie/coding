#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160826

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        num_s = []
        operators = ["+", "-", "("]
        i = 0
        while i < s_len:
            # 跳过空格
            if s[i] == " ":
                i += 1
                continue
            # 操作符直接入栈
            elif s[i] in operators:
                num_s.append(s[i])
                i += 1
            else:
                # 右括号入栈
                if s[i] == ")":
                    num_s.append(s[i])
                    i += 1
                else:
                    # 遇到数字
                    temp = 0
                    # 将数字字符串变换成整数
                    while i < s_len and ("0"<=s[i]<="9"):
                        temp = temp * 10 + int(s[i])
                        i += 1
                    # 数字入栈
                    num_s.append(temp)
                # 处理栈内元素
                self.compute(num_s, operators)

        return num_s[0] if num_s else 0


    def compute(self, num_s, operators):
        # 空栈则返回
        if not num_s:
            return
        # 首字符为操作符
        if (num_s[-1] in operators):
            return
        # 处理有括号
        elif num_s[-1] == ")":
            # 两个括号中有数字
            if num_s[-2] != "(":
                # 保留数字
                num_s[-3] = num_s[-2]
            num_s.pop()
            num_s.pop()
            # 处理 3+(4+5)，括号中元素处理后3+9，应该继续计算
            self.compute(num_s, operators)
        else:
            # 栈中元素只有一个直接返回
            if len(num_s) >= 2:
                # 获取操作符
                operator = num_s[-2]
                # 处理加法
                if operator == "+":
                    num_s[-3] = num_s[-3] + num_s[-1]
                # 处理减法
                elif operator == "-":
                    # print num_s
                    num_s[-3] = num_s[-3] - num_s[-1]
                # 遇到左括号
                elif operator == "(":
                    return
                # else:
                #     num_s[-2] = num_s[-2] * 10 + num_s[-1]
                #     num_s.pop()
                #     return
                num_s.pop()
                num_s.pop()

s = "(1+(4+5+22)-3) + ( 6+8)"
# s = "2147483647"
# s = "1-11"
s = "()"
so = Solution()
print so.calculate(s)
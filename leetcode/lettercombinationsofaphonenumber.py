#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160702

class Solution(object):
    num2letter = {"0":[" "], "1":["*"],  "2":["a", "b", "c"], "3":["d", "e", "f"], 
        "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], 
        "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

如果在给定num2letter的情况下，就是将每个数字对应的字母组合在一起
        """

        if not digits:
            return []
        ret = self.recursive_combine(digits)
        return ret

    def recursive_combine(self, digits):
        letters = self.num2letter[digits[0]]
        result = []
        if len(digits) > 1:
            result = self.recursive_combine(digits[1:])
        ret = []
        for i in letters:
            if result:
                for j in result:
                    ret.append(i+j)
            else:
                ret.append(i)
        return ret

digits = "18363120"
so = Solution()
print so.letterCombinations(digits)
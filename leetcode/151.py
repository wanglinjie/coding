#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160809

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
        """
        s_list = s.split()
        s_list = s_list[::-1]
        return " ".join(s_list)
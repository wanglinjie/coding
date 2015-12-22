#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20151222
Last Modified: 
判断两个字符串是否是同字母构成的异序词
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = sorted(s)
        t_list = sorted(t)
        if s_list == t_list:
            return True
        else:
            return False
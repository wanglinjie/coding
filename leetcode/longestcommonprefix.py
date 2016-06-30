#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160630
import sys
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = 0
        str_num = len(strs)
        if (not str_num):
            return ""

        min_len = sys.maxint

        # 记录这些字符串中最短字符串长度
        for i in strs:
            str_len = len(i)
            if str_len < min_len:
                min_len = str_len

        # 每个字符串中第几个字符
        for i in xrange(min_len):
            is_equal = True
            # 遍历字符串，判断字符串第i位字符是否相同
            for j in xrange(1, str_num):
                if strs[j][i] != strs[0][i]:
                    is_equal = False
                    break
            if is_equal:
                # 如果第i位所有字符串都相同则记录目前位置最长前缀字符串位置
                ret += 1
            else:
                # 如果不相同在跳出循环
                break
        # print ret
        # 返回最长前缀字符串
        return strs[0][0:ret]

# strs = ["aaa", "aab", "abc"]
strs = ["aca","cba"]
so = Solution()
print so.longestCommonPrefix(strs)
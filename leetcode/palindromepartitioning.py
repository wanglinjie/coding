#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160802

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
        """
        ret = self.recursivePartition(s, {})
        return ret

    def recursivePartition(self, s, record):
        # record记录字符串可能的回文组合
        if not s:
            return []
        s_len = len(s)
        ret = []
        for i in xrange(s_len):
            if self.isPalindrome(s[0:i+1]):
                if s[i+1:] in record:
                    # 如果字符串在record中有记录，则直接使用记录
                    temp_result = record[s[i+1:]]
                else:
                    # 否则递归切分字符串
                    temp_result = self.recursivePartition(s[i+1:], record)
                    record[s[i+1:]] = temp_result
                for j in temp_result:
                    ret.append([s[0:i+1]] + j)
                if not temp_result:
                    ret.append([s[0:i+1]])
        return ret
                
    def isPalindrome(self, s):
        # 判断字符串是否为回文
        if not s:
            return True
        start = 0
        end = len(s)-1
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
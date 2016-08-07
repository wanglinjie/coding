#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160807

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool

Given a string s and a dictionary of words dict, 
determine if s can be segmented into a space-separated sequence 
of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

思路：
遍历s字符串，判断子串是否在wordDict中出现，出现则遍历剩余字串
使用字典存储已经判断的子串，避免多次判断
        """

        # 下面递归实现，但是超时
        s_len = len(s)
        if not s_len:
            return True
        words = set()
        for i in wordDict:
            for j in i:
                words.add(j)
        for i in s:
            if i not in words:
                return False
        return self.recursiveWord(s, wordDict, {})

    def recursiveWord(self, s, wordDict, records):
        s_len = len(s)
        if not s_len:
            return True
        for i in xrange(s_len):
            if s[:i+1] in wordDict:
                if s[:i+1] in records:
                    result = records[s[:i+1]]
                else:
                    result = self.recursiveWord(s[i+1:], wordDict, records)
                    records[s[:i+1]] = result
                if result:
                    return True
        return False


s= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
# s = "leetcode"
# wordDict = ["leet", "code"]
so = Solution()
print so.wordBreak(s, wordDict)
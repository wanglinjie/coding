#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160807

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

Given a string s and a dictionary of words dict, 
add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

思路和word break类似，只是需要存储每种可能情况
        """
        result = self.recursiveWord(s, wordDict, {})
        return result;
    
    def recursiveWord(self, s, wordDict, records):
        s_len = len(s)
        if not s_len:
            return [""]
        ret = []
        for i in xrange(s_len):
            sub_str = s[:i+1]
            if sub_str in wordDict:
                if s[i+1:] in records:
                    result = records[s[i+1:]]
                else:
                    result = self.recursiveWord(s[i+1:], wordDict, records)
                    records[s[i+1:]] = result
                for i in result:
                    if i:
                        ret.append(sub_str + " " + i)
                    else:
                        ret.append(sub_str)
        return ret
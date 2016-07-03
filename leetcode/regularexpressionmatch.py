#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160703

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

暴力解决：
基本思路就是先看字符串s和p的从i和j开始的子串是否匹配，用递归的方法直到串的最后，最后回溯回来得到结果。假设现在走到s的i位置，p的j位置，情况分为下列两种： 
(1)p[j+1]不是'*'。情况比较简单，
只要判断当前s的i和p的j上的字符是否一样（如果有p在j上的字符是'.',也是相同），如果不同，返回false，
否则，递归下一层i+1，j+1; 
(2)p[j+1]是'*'。那么此时看从s[i]开始的子串，
假设s[i],s[i+1],...s[i+k]都等于p[j]那么意味着这些都有可能是合适的匹配，
那么递归对于剩下的(i,j+2),(i+1,j+2),...,(i+k,j+2)都要尝试（j+2是因为跳过当前和下一个'*'字符）。 
实现代码如下：
        """
        return self.recursive_match(s, p, 0, 0)

    def recursive_match(self, s, p, i, j):
        if j == len(p):
            return i == len(s)

        # p中下一个字符不是“*”
        if (j == (len(p)-1)) or (p[j+1] != "*"):
            # 当前字符不相等
            if (i == len(s) or (s[i] != p[j] and p[j] != ".")):
                return False
            else:
                # 当前字符相等
                return self.recursive_match(s, p, i+1, j+1)
        # 如果下一个字符是“*”
        while (i < len(s)) and (p[j] == "." or (s[i] == p[j])):
            if self.recursive_match(s, p, i, j+2):
                return True
            i += 1
        return self.recursive_match(s, p, i, j+2)

s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
so = Solution()
if so.isMatch(s, p):
    print "True"
else:
    print "False"

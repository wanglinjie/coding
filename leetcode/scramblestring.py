#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160725
import collections
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool


Given a string s1, we may represent 
it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, 
it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", 
it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, 
determine if s2 is a scrambled string of s1.
        """
        return self.recursiveScramble(s1, s2, {})

    def recursiveScramble(self, s, t, memo):
        if len(s) != len(t):
            return False
        if len(s) <= 1:
            return s == t
        if (s, t) in memo:
            return memo[s, t]
        for i in range(1, len(s)):
            # 递归判断s1和s2左右两侧是否为scramble
            if (self.recursiveScramble(s[:i], t[-i:], memo) and self.recursiveScramble(s[i:], t[:-i], memo)) or\
               (self.recursiveScramble(s[:i], t[:i], memo) and self.recursiveScramble(s[i:], t[i:], memo)):
                   memo[s,t] = True
                   return True
        memo[s, t] = False
        return False


s1 = "great"
s2 = "rgtae"
so = Solution()
print so.isScramble(s1, s2)
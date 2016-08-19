#/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160819

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true
        """
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        # 记录第一个字符串中字母到到第二个字符串字母的映射
        char_dic = {}
        # 记录已经使用的第二个字符串的字母
        value_set = set()

        # 遍历两个字符串中字母
        for i in xrange(s_len):
            # 如果s[i]在s中第一次出现
            if s[i] not in char_dic:
                # 如果t[i]这个字母已经是s中另一个字母的映射，则不能是s[i]的映射
                if t[i] in value_set:
                    return False

                # 保存字母到字母的映射
                char_dic[s[i]] = t[i]
                # 保存t[i]字母
                value_set.add(t[i])
            else:
                # 如果s中相同两个字母的对应映射不一样，则返回False
                if char_dic[s[i]] != t[i]:
                    return False
        return True

s = "pape"
t = "title"
so = Solution()
print so.isIsomorphic(s, t)
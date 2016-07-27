#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160727
import copy
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string 
which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
        """
        s_dic = {}
        for i in xrange(len(s)):
            if s[i] not in s_dic:
                s_dic[s[i]] = []
            s_dic[s[i]].append(i)
        num = self.countDistinct(s_dic, t, [], {})
        return num

    def countDistinct(self, s_dic, t, record1, record2):
        '''
        record1记录到目前位置在s中取的最大位置
        record2记录以(t的子串, 子串当前在s中取的最大位置)为key
        记录s[i+1:], t[j+1:]的countDistinct次数,其中j+1为t中剩余子串起始位置
        i+1为s中剩余子串起始位置
        '''
        if not t:
            return 0
        value = t[0]
        ret = 0
        if value not in s_dic:
            return 0
        for i in xrange(len(s_dic[value])):
            if record1 and (record1[-1] >= s_dic[value][i]):
                continue
            if len(t) == 1:
                num = 1
            else:
                
                key = (t[1:], s_dic[value][i])
                if key in record2:
                    num = record2[key]
                else:
                    temp = s_dic[value]
                    # 将value的出现列表减少，避免之后不必要的遍历判断
                    s_dic[value] = s_dic[value][i+1:]
                    # num = self.countDistinct(s_dic, t[1:], record1 + [temp[i]], record2)
                    num = self.countDistinct(s_dic, t[1:], [temp[i]], record2)
                    s_dic[value] = temp

                    record2[key] = num

            ret += num
        return ret


s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
t = "bddabdcae"
# s = "helloh"
# t = ""
so = Solution()
print so.numDistinct(s, t)
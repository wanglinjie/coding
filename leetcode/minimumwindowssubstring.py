#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160723
import sys
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

Given a string S and a string T, 
find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, 
you are guaranteed that there will always be only one unique minimum window in S.


The current window is s[i:j] and the result window is s[I:J]. 
In need[c] I store how many times I need character c (can be negative) and 
missing tells how many characters are still missing. 
In the loop, first add the new character to the window. 
Then, if nothing is missing, 
remove as much as possible from the window start and then update the result.
        """
    #     if not t:
    #         return ""
    #     s_dic = {}
    #     t_dic = {}
    #     for i, j in enumerate(s):
    #         if j not in s_dic:
    #             s_dic[j] = []
    #         s_dic[j].append(i)
    #     for i, j in enumerate(t):
    #         if j not in t_dic:
    #             t_dic[j] = 0
    #         t_dic[j] += 1
    #     t_list = []
    #     for i in t_dic:
    #         if (i not in s_dic) or (t_dic[i] > len(s_dic[i])):
    #             return ""
    #         t_list.append(s_dic[i])
        
    #     ret_min_pos, ret_max_pos = self.recursiveFindWindow(t_list, 0, [])
    #     return s[ret_min_pos:ret_max_pos+1]
    
    # def recursiveFindWindow(self, t_list, num, positions):
    #     if num == len(t_list):
    #         min_pos = min(positions)
    #         max_pos = max(positions)
    #         return min_pos, max_pos 
    #     ret_min_pos = 0
    #     ret_max_pos = sys.maxint
    #     min_windows = sys.maxint
    #     for i in t_list[num]:
    #         min_position, max_position = self.recursiveFindWindow(t_list, num+1, positions+[i])
    #         result = max_position - min_position
    #         if result < min_windows:
    #             min_windows = result
    #             ret_min_pos = min_position
    #             ret_max_pos = max_position
    #     return ret_min_pos, ret_max_pos
        # need 中存储t中对应字符的出现次数
        # missing存储字符串总长度
        need, missing = collections.Counter(t), len(t)
        # i 是开始位置
        i = I = J = 0
        # 遍历s中字符
        for j, c in enumerate(s, 1):
            # 当这个字符出现在t中，并且need[c]>0,则missing减1
            missing -= need[c] > 0
            # 对应字符出现次数减1
            need[c] -= 1
            # 如果t中所有字符都在s中出现了，则进入判断
            if not missing:
                # need[s[i]]<0表示s中第i位的字符在i后还出现了，可以用之后出现字符代替
                # need[s[i]]<0也有种可能是这个字符在t中没有出现
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]



s = "a"
t = "aabc"
so = Solution()
print so.minWindow(s, t)

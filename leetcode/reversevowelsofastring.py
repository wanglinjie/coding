#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160615

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
        """
        s_list = list(s)
        s_len = len(s_list)
        if s_len <= 1:
            return s

        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # vowels_dic = {}
        # for i in vowels:
        #     vowels_dic[i] = True
        vowels_dic = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True, 'A':True, 'E':True, 'I':True, 'O':True, 'U':True}
        

        '''
        下面方法是将字符串中元音字母提取出来，单独将元音字母倒置，然后重新写入字符列表中
        '''
        vowels_list = []
        vowels_position = []
        for i in xrange(s_len):
            if s_list[i] in vowels_dic:
                vowels_list.append(s_list[i])
                vowels_position.append(i)
        vowels_len = len(vowels_list)
        # vowels_position.reverse()
        for i in xrange(vowels_len):
            s_list[vowels_position[vowels_len-1-i]] = vowels_list[i]
            # s_list[vowels_position[i]] = vowels_list[i]
        return "".join(s_list)

s = "leetcOde"
so = Solution()
print so.reverseVowels(s)
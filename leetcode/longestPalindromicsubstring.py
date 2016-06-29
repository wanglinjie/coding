#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160629

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
        """

        '''
        下面是使用蛮力算法
        回文情况分两种：
        一种是：回文中元素个数为奇数个，这时以中间节点为中心，向两侧扩散
        第二种是：回文中元素个数为偶数个，这时中间两个节点应该相等
        '''
        s_len = len(s)
        # 如果字符串中元素为空或者只有一个，则直接返回
        if (not s_len) or (s_len == 1):
            return s
        longest = ""

        # 遍历字符串中每个元素，以该元素中中心节点
        for i in xrange(0, s_len-1):
            j = 0
            left = i - j
            right = i + j

            # 当回文个数为奇数个时，向两侧遍历
            while (left >= 0) and (right < s_len):
                if s[left] != s[right]:
                    break
                j += 1
                left = i - j
                right = i + j
            # print j
            palindrome_len = 2 * (j-1) + 1
            if palindrome_len > len(longest):
                # longest = palindrome_len
                longest = s[i-j+1:i+j]

            # 当回文元素为偶数个时，向两侧遍历
            if (i+1<s_len) and (s[i] == s[i+1]):
                # print "he", i
                j = 0
                left = i - j
                right = i + 1+ j
                while (left >= 0) and (right < s_len):
                    if s[left] != s[right]:
                        break
                    j += 1
                    left = i - j
                    right = i + 1 + j
                palindrome_len = 2 * j
                if palindrome_len > len(longest):
                    # longest = palindrome_len
                    longest = s[i-j+1:i+1+j]
                    # print "if ", len(longest)
                # else:
                #     print "else ", len(longest)
                #     print palindrome_len
        return longest

# s = "abccba"
s = "a"
# print s
so = Solution()
ret = so.longestPalindrome(s)
print ret
print len(ret)







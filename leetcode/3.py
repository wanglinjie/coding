#/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160509

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
        """
        # longest_length = 0
        # s_list = list(s)
        # temp_list = []
        # for i in s_list:
        #     if i in temp_list:
        #         if len(temp_list) > longest_length:
        #             longest_length = len(temp_list)
        #         i_index = temp_list.index(i)
        #         del temp_list[0:i_index + 1]
        #     temp_list.append(i)
        # if len(temp_list) > longest_length:
        #     longest_length = len(temp_list)
        # return longest_length
        s_len = len(s)
        if not s_len:
            return 0
        max_length = 0
        temp_c = {}
        j = 0
        for i in xrange(s_len):
            if s[i] in temp_c:
                j = max(temp_c[s[i]]+1, j)
            temp_c[s[i]] = i
            max_length = max(max_length, i-j+1)
        return max_length







        # s_list = list(s)
        # longest_length = 0
        # temp_string = ""

        # for i in s:
        #     if i not in temp_string:
        #         temp_string += i
        #     else:
        #         if len(temp_string) > longest_length:
        #             longest_length = len(temp_string)
        #         temp_string = i
        # if len(temp_string) > longest_length:
        #     longest_length = len(temp_string)
        # return longest_length


s = "asdfskdajsfkaas"
so = Solution()
print so.lengthOfLongestSubstring(s)
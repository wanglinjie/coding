#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160725

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
        """
        return self.recursiveDecodings(s, {})
    def recursiveDecodings(self, s, records):
        if s in records:
            return records[s]
        s_len = len(s)
        if s_len <= 0:
            return 0
        elif s_len == 1:
            if s == "0":
                return 0
            records[s] = 1
            return 1
        have_single_num = 0
        have_two_num = 0
        # 首位为0则返回0，因为0没有对应字母
        if s[0] == "0":
            return 0
        # 如果第二个数字为0，则只能同时取两位，否则可以只取一位
        if s[1] != "0":
            have_single_num = self.recursiveDecodings(s[1:], records)
        # 取两位数字
        two_num = int(s[:2])
        if two_num <= 26:
            if s_len == 2:
                # 如当前s只剩下两位则只有一种取法
                have_two_num = 1
            else:
                have_two_num = self.recursiveDecodings(s[2:], records)
        total_num = have_single_num + have_two_num
        records[s] = total_num
        print s, total_num
        return total_num


s = "26"
so = Solution()
print so.numDecodings(s)
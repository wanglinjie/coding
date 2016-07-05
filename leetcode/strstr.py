#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160705

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

Implement strStr().

Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
        """
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1
        haystack_len = len(haystack)
        needle_len = len(needle)
        if haystack_len < needle_len:
            return -1
        elif needle_len == 0:
            return 0
        for i in xrange(haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1


haystack = "basdsdfa"
needle = "a"
so = Solution()
print so.strStr(haystack, needle)
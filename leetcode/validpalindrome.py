#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160730

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? 
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
        """
        s_len = len(s)
        if not s_len:
            return True
        new_s = s.lower()
        i = 0
        j = s_len - 1
        while (i <= j):
            while (i <= j):
                if ((new_s[i] >= "a" and new_s[i] <= "z") or (new_s[i] >= "0" and new_s[i] <= "9")):
                    break
                i += 1
            while (i <= j):
                if ((new_s[j] >= "a" and new_s[j] <= "z") or (new_s[j] >= "0" and new_s[j] <= "9")):
                    break
                j -= 1
            if (i <= j) and (new_s[i] != new_s[j]):
                return False
            i += 1
            j -= 1
        return True

s = "h00h"
so = Solution()
print so.isPalindrome(s)
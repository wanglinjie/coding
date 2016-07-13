#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160712

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.
        """
        # try:
        #     ret = float(s)
        #     return True
        # except:
        #     return False
        s = s.lower().strip()
        if not s:
            return False
        if len(s) > 1:
            if s[0] == "-":
                s = s[1:]
            elif s[0] == "+":
                s = s[1:]
        if "e" in s:
            s_split = s.split("e")
            if len(s_split) != 2:
                return False
            if "." in s_split[1]:
                return False
            if len(s_split[1]) > 1:
                if s_split[1][0] == "-":
                    s_split[1] = s_split[1][1:]
                elif s_split[1][0] == "+":
                    s_split[1] = s_split[1][1:]

            if (not s_split[0]) or (not s_split[1]):
                return False
            if self.isFloat(s_split[0]) and self.isFloat(s_split[1]):
                return True
            else:
                return False
        else:
            if self.isFloat(s):
                return True
            else:
                return False

    def isFloat(self, s):
        if "." not in s:
            for i in s:
                if (i < "0") or (i > "9"):
                    return False
            return True
        else:
            if s == ".":
                return False
            s_split = s.split(".")
            if len(s_split) != 2:
                return False
            if self.isFloat(s_split[0]) and self.isFloat(s_split[1]):
                return True
            else:
                return False


        

s = " 005047e+"
so = Solution()
print so.isNumber(s)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160626

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

思路简单，就是遍历字符串，如果是左括号则入栈，如果是右括号则判断栈顶是否和当前括号成对
如果成对则栈顶元素弹出
如果不成对，则返回False
        """
        if not s:
            return True
        s_stack = []
        left_bracket = ["(", "{", "["]
        right_bracket = [")", "}", "]"]
        for i in s:
            if i in left_bracket:
                s_stack.append(i)
            else:
                if s_stack:
                    i_index = right_bracket.index(i)
                    if s_stack[-1] == left_bracket[i_index]:
                        del s_stack[-1]
                    else:
                        return False
                else:
                    return False
        if len(s_stack):
            return False
        else:
            return True


s = "[]"
so = Solution()
if so.isValid(s):
    print "True"
else:
    print "False"
# -*- coding:utf-8 -*-
# date:20160516

'''Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
不使用循环或者递归的情况，可以判断数num中有几个1，以及1所在位置
4的幂中只有一个1，而且1所在的位置应该是奇数位上
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        result = 1
        while result < num:
            result = result << 2
            if result == num:
                return True
        return False



so = Solution()
if so.isPowerOfFour(64):
    print "True"
else:
    print "False"
#!/usr/bin/env python
#-*-coding:utf-8-*-
'''

@author:    Wanglj
@date:  2015.12.17
'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = n % 4
        if number:
            return True
        else:
            return False

solu = Solution()
print solu.canWinNim(11)
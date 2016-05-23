# -*- coding:utf-8 -*-
'''
解决思想是：奇数a中1的个数都是偶数(a-1)中1个数加1
偶数中1的个数和偶数除2中1的个数相等。（因为b中1个数是i，则b*2是将b左移1位，1的个数不变）
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num_list = [0] * (num+1)
        for i in xrange(1, num+1):
            if i % 2:
                num_list[i] = num_list[i-1] + 1
            else:
                num_list[i] = num_list[(i/2)]
        return num_list

so = Solution()
num = 5
print so.countBits(num)
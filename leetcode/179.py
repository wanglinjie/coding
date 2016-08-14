#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160814


'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

可以将数组中数字排序，排序的规则是如果ab拼接比ba拼接大，则a比b大
'''
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return "0"
        nums_str = [str(i) for i in nums]
        nums_str = sorted(nums_str, cmp=self.compare, reverse=True)
        ret = "".join(nums_str)
        # 防止出现首位为0情况
        ret = str(int(ret))
        return ret
    
    def compare(self, a, b):
        ab = int(a+b)
        ba = int(b+a)
        if ab > ba:
            return 1
        elif ab < ba:
            return -1
        else:
            return 0

nums = [3, 30, 34, 5, 9]
so = Solution()
print so.largestNumber(nums)
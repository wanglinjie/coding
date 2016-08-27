#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160827

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        if not nums_len:
            return []
        left = [1] * nums_len
        right = [1] * nums_len
        
        lvalue = 1
        rvalue = 1
        for i in xrange(1, nums_len):
            left[i] = left[i-1] * nums[i-1]
            right[nums_len-i-1] = right[nums_len-i] * nums[nums_len-i]
        ret = [right[0]]
        for i in xrange(1, nums_len-1):
            ret.append(left[i] * right[i])
        if nums_len > 1:
            ret.append(left[nums_len-1])
        return ret

nums = []
so = Solution()
print so.productExceptSelf(nums)
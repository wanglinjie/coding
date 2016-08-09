#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160809

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
        """
        if not nums:
            return 0
        ret = nums[0]
        maxNum = nums[0]
        minNum = nums[0]
        for i in xrange(1, len(nums)):
            local_max = maxNum
            local_min = minNum
            maxNum = max(max(nums[i], local_max * nums[i]), local_min * nums[i])
            minNum = min(min(nums[i], local_min * nums[i]), local_max * nums[i])
            if maxNum > ret:
                ret = maxNum
        return ret
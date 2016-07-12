#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160711

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Find the contiguous subarray within an array (containing at least one number) 
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

思路：
动态规划思想，寻找子数组中元素和最大
如果第i-1个元素和i-1之前元素组成的连续数组和小于0，则第i个元素就没有必要和第i个元素之前的组合

使用一个额外数组，数组第i个位置记录nums中包含第i个元素的连续数组加和最大的和，
和第i个元素相加的元素排在第i个元素前
        """
        nums_len = len(nums)
        largest_nums = [0] * nums_len
        largest_nums[0] = nums[0]
        for i in xrange(1, nums_len):
            largest_nums[i] = max(nums[i], largest_nums[i-1]+nums[i])
        return max(largest_nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
so = Solution()
print so.maxSubArray(nums)
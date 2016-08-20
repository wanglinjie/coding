#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160820

import sys

class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

Given an array of n positive integers and a positive integer s, 
find the minimal length of a subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

思路：
题目是要一个子数组和大于等于s，所以元素是连续的加和
        """
        low = 0
        total = 0
        nums_len = len(nums)
        ret = nums_len + 1

        # 遍历数组中每个元素
        for high in xrange(nums_len):
            # 添加该元素
            total += nums[high]

            # 如果加和大于等于s
            while total >= s:
                # 获取到目前最小的距离
                ret = min(ret, high - low + 1)

                # 当前加和已经大于等于s，则添加下一个元素时，就不需要low位置上的元素
                total -= nums[low]
                low += 1
        if ret == (nums_len + 1):
            return 0
        else:
            return ret

s = 100
nums = []
so = Solution()
print so.minSubArrayLen(s, nums)
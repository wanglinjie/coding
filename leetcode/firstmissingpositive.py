#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

题目是查找第一个缺失的正整数，这意思是从1开始
思路：列表中的数字按顺序排列
        """
        n = len(nums)
        if n <= 0:
            return 1
        for i in xrange(n):
            while (nums[i] != i+1) and (nums[i] < n) and (nums[i] > 0) and (nums[i] != nums[nums[i] - 1]):
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in xrange(n):
            if i != nums[i]-1:
                return i + 1
        return n + 1


nums = [3,4,-1,1]
so = Solution()
print so.firstMissingPositive(nums)


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160714

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

Given an array with n objects colored red, 
white or blue, sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
        """
        counts = [0] * 3
        # 统计每种颜色出现次数
        for i in nums:
            counts[i] += 1
        start = 0

        # 按照每种颜色出现次数，将nums中相应数字改为对应颜色数字
        for i in range(3):
            for j in xrange(start, start+counts[i]):
                nums[j] = i
            # nums[start:start+counts[i]] = [i] * counts[i]
            start += counts[i]



nums = [0, 1, 2, 1, 1, 1, 2, 2, 1]
so = Solution()
so.sortColors(nums)
print nums
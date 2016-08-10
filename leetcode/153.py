#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160810

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
        """
        if not nums:
            return 0
        nums_len = len(nums)
        low = 0
        high = nums_len - 1
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]
            middle = low + (high - low) / 2
            if nums[high] < nums[middle]:
                low = middle + 1
            else:
                high = middle
        return nums[low]
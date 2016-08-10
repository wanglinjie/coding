#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160810

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            middle = low + (high - low)/2
            if nums[middle] > nums[high]:
                low = middle + 1
            elif nums[middle] < nums[high]:
                high = middle
            else:
                high -= 1
        return nums[low]
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160709

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

思路：
就是一个二分查找target，找到就直接返回它的位置
如果没有找到，则left指针指向位置就是它的相应位置
        """
        nums_len = len(nums)
        left = 0
        right = nums_len - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

nums = [1]
target = 0
so = Solution()
print so.searchInsert(nums, target)
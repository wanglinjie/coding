#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160724

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
        """
        nums_len = len(nums)
        left = 0
        right = nums_len - 1
        while (left < right):
            middle = left + (right - left) / 2
            if (nums[middle] == target):
                return True
            if nums[middle] > nums[right]:
                if (nums[middle] > target) and (nums[left] <= target):
                    right = middle
                else:
                    left = middle + 1
            elif nums[middle] < nums[right]:
                if (nums[middle] < target) and (nums[right] >= target):
                    left = middle + 1
                else:
                    right = middle
            else:
                right -= 1

        return nums[left] == target

nums = [1, 3]
target = 2
so = Solution()
print so.search(nums, target)

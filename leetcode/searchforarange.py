#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160708

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]
        """
        nums_len = len(nums)
        if not nums_len:
            return [-1, -1]
        start = 0
        end = nums_len - 1
        result = []
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        result.append(start)

        start = 0
        end = nums_len - 1
        while start <= end:
            mid = start + (end - start) / 2
            if (nums[mid] > target):
                end = mid - 1
            else:
                start = mid + 1
        result.append(end)
        if result[0] > result[1]:
            return [-1, -1]
        else:
            return result


a = [8] * 20
target = 7
so = Solution()
print so.searchRange(a, target)

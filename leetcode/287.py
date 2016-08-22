#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160822

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Given an array nums containing n + 1 integers where each integer is 
between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, 
but it could be repeated more than once.
        """
        nums_len = len(nums)
        low = 1
        high = nums_len - 1
        while low < high:
            middle = low + (high - low)/2
            count = 0
            for i in nums:
                if i <= middle:
                    count += 1
            if count <= middle:
                low = middle + 1
            else:
                high = middle
        return low
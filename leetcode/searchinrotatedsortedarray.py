#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160706

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
        """
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left+(right-left)/2
            lv = nums[left]
            mv = nums[mid]
            rv = nums[right]

            if (lv < target < mv) or (mv < lv < target) or (target < mv < rv):
                # 右侧指针左移
                right = mid - 1
            elif (lv < mv < target) or (target < rv < mv) or (mv < target < rv):
                # 左侧指针右移
                left = mid + 1
            else:
                break
        if target == lv:
            return left
        elif target == mv:
            return mid
        elif target == rv:
            return right
        else:
            return -1
            
        # return left if (target==lv) else mid if (target==mv) else right if target==rv else -1

nums = [4, 5, 6, 7, 1, 2, 3]
target = 6
so = Solution()
print so.search(nums, target)
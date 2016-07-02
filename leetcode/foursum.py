#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160702

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]

Given an array S of n integers, are there elements a, b, c, 
and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

下面实现的思路是借助于3sum，将4sum分解成求3sum
        """
        nums_len = len(nums)
        if nums_len < 4:
            return []
        ret = []
        nums.sort()
        for i in xrange(nums_len-3):
            remain = target - nums[i]
            result = self.threeSum(nums[i+1:], remain)
            if result:
                for j in result:
                    j.insert(0, nums[i])
                    if j not in ret:
                        ret.append(j)
        return ret

    def threeSum(self, nums, target):
        nums_len = len(nums)
        ret = []
        for i in xrange(nums_len-2):
            low = i + 1
            high = nums_len - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                if three_sum == target:
                    # temp = [nums[i], nums[low], nums[high]]
                    ret.append([nums[i], nums[low], nums[high]])
                    # print ret
                    low += 1
                    high -= 1
                elif three_sum < target:
                    low += 1
                else:
                    high -= 1
        return ret

nums = [1, 0]
target = 0
so = Solution()
print so.fourSum(nums, target)
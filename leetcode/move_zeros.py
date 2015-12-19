#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20151219
Last Modified: 
获取树的最大深度
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        site = 0
        for i in nums:
            if i:
                nums[site] = i
                site += 1
        if site < len(nums):
            nums[site:] = [0] * (len(nums) - site)

nums = [0, 1, 0, 3, 12]
so = Solution()
so.moveZeroes(nums)
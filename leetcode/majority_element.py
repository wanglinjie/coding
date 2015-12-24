#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20151224
Last Modified: 
获得出现次数超过n/2次的项
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for i in num_dict:
            if num_dict[i] > (len(nums) / 2):
                return i
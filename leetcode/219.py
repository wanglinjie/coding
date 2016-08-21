#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160821

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the difference between i and j is at most k.
        """
        nums_len = len(nums)
        num_dic = {}
        for i in xrange(nums_len):
            if nums[i] not in num_dic:
                num_dic[nums[i]] = i
            else:
                if (i - num_dic[nums[i]]) <= k:
                    return True
                num_dic[nums[i]] = i
        return False
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160901

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_dic = collections.Counter(nums)
        for i in nums_dic:
            if nums_dic[i] == 1:
                return i
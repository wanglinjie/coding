#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160611

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
        """
        if (not nums1) or (not nums2):
            return []
        dict_1 = {}
        ret_dic = {}
        ret = []
        for i in nums1:
            dict_1[i] = True
        for i in nums2:
            if i in dict_1:
                ret_dic[i] = True
        for i in ret_dic:
            ret.append(i)
        return ret

nums1 = [1, 2, 2, 1]
nums2 = [3]
so = Solution()
print so.intersection(nums1, nums2)
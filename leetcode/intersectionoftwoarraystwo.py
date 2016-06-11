#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160611

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]


Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, 
and the memory is limited such that you cannot load all elements into the memory at once?
        """
        if (not nums1) or (not nums2):
            return []
        dict_1 = {}
        ret = []
        for i in nums1:
            if i not in dict_1:
                dict_1[i] = 0
            dict_1[i] += 1
        for i in nums2:
            if i in dict_1:
                ret.append(i)
                dict_1[i] -= 1
                if dict_1[i] == 0:
                    del dict_1[i]
        return ret

nums1 = [1, 2, 3, 2, 1]
nums2 = [2, 2, 3]
so = Solution()
print so.intersect(nums1, nums2)
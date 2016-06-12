#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160612

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]


Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

思路是：先使用字典存储每个数字出现的次数
然后按照出现次数对数字进行排序
选取前K个数字

改进：
不直接对所有单独数字排序，而是直接使用堆存储
        """
        if not nums:
            return []
        element_dic = {}
        ret = []
        for i in nums:
            if i not in element_dic:
                element_dic[i] = 0
            element_dic[i] += 1
        sort_list = sorted(element_dic, key=element_dic.__getitem__, reverse=True)
        return sort_list[:k]


nums = [1,1,1,2,2,3]
k = 1
so = Solution()
print so.topKFrequent(nums, k)
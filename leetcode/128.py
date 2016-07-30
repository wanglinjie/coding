#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160730

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
        """
        #  set中查找元素平均复杂度是o(1)
        nums = set(nums)
        ret = 0
        for i in nums:
            # 如果i-1不在nums中
            if (i-1) not in nums:
                m = i + 1
                # 获取从当前i之后的连续数字个数
                while m in nums:
                    m += 1
                if m - i > ret:
                    ret = m - i
        return ret
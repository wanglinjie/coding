#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160603
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]


Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
        """
        nums_len = len(nums)
        if not nums_len:
            return [[]]
        nums = sorted(nums)
        ret = [[]]
        for num in nums:
            ret_len = len(ret)
            for i in xrange(ret_len):
                temp = ret[i] + [num]
                if temp not in ret:
                    ret.append(temp)
        return ret


nums = [1]
so = Solution()
print so.subsetsWithDup(nums)
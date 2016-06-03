#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160603
import copy
import time
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
        """
        start = time.time()
        nums_len = len(nums)
        if not nums_len:
            return [[]]
        nums = sorted(nums)
        ret = [[]]
        # last = [[]]
        for num in xrange(nums_len):
            temp = [nums[num]]
            now = copy.deepcopy(ret)
            for i in ret:
                now.append(i+temp)
            ret = now
        print time.time() - start
        return ret
            

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
so = Solution()
print so.subsetsWithDup(nums)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160715

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
        """
        if (n < k) or (k <= 0):
            return [[]]
        nums = [i+1 for i in xrange(n)]
        result = self.recursiveCombine(nums, k)
        return result

    def recursiveCombine(self, nums, k):
        ret = []
        nums_len = len(nums)
        # for i in nums[:(nums_len-k+1)]:
        for i in xrange(nums_len-k+1):
            if k > 1:
                result = self.recursiveCombine(nums[i+1:], k-1)
                for j in result:
                    j.insert(0, nums[i])
                    ret.append(j)
            else:
                ret.append([nums[i]])
        return ret



n = 5
k = 6
so = Solution()
print so.combine(n, k)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160710

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

Given a set of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

思路：
递归调用combinationSum函数，求新target的组合求和
        """
        ret = []
        for i in candidates:
            if i == target:
                # 当i等于target则直接存储这个
                ret.append([i])
            elif i < target:
                # 如果i值小于target，则可以尝试将i作为target组合中一个元素
                results = self.combinationSum(candidates, target-i)
                for j in results:
                    if j[0] >= i:
                        ret.append([i] + j)
        return ret

candidates = [1]
target = 7
so = Solution()
print so.combinationSum(candidates, target)
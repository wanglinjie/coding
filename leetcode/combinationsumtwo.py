#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160710

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

思路和combinationSum类似，只是这次不能重复使用一个数字
在递归过程中，传递的candidates应该去掉当前这个字
因为输入candidates是乱序的，可以将candidates排序
递归过程中将当前元素之后的元素输入，这样可以避免多次判断
        """

        # 输入元素排序
        candidates.sort()
        ret = self.combinationSum(candidates, target)
        return ret
    def combinationSum(self, candidates, target):
        ret = []
        candidates_len = len(candidates)
        for i in xrange(candidates_len):
            # 尝试将输入的每个元素作为结果中一个元素
            if candidates[i] == target:
                temp = [candidates[i]]
                if temp not in ret:
                    ret.append([candidates[i]])
            elif candidates[i] < target:
                results = []
                if i < candidates_len - 1:
                    results = self.combinationSum(candidates[i+1:], target-candidates[i])
                for j in results:
                    temp = [candidates[i]] + j
                    if temp not in ret:
                        ret.append(temp)
        return ret


candidates = [1,1]
target = 1
# target = 123
so = Solution()
print so.combinationSum2(candidates, target)
                
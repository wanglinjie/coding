# date:20160526
# -*- coding:utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
        """
        # 注意题目中并没有说列表是有序的，所以是无序排列的
        n = len(nums)
        return (n * (n+1) >> 1) - sum(nums)

nums = [0, 1, 3]
so = Solution()
print so.missingNumber(nums)
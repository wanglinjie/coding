#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160623

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

Given an array of numbers nums, 
in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?
        """

        # 下面的实现比较low，没有按照要求来，使用空间为o(n)
        nums_dic = {}
        for i in nums:
            if i not in nums_dic:
                nums_dic[i] = 0
            nums_dic[i] += 1
        ret = []
        for i in nums_dic:
            if nums_dic[i] == 1:
                ret.append(i)
        if ret:
            return ret
        else:
            return [0, 0]

nums = [1, 1, 2]
so = Solution()
print so.singleNumber(nums)
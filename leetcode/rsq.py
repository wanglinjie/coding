# -*- coding:utf-8 -*-

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.nums_len = len(nums)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i >= self.nums_len:
            return False
        self.nums[i] = val
        return True
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i > j) or (i < 0) or (j >= self.nums_len):
            return 0
        num = 0
        for x in xrange(i, j+1):
            num += self.nums[x]
        return num



so = NumArray()

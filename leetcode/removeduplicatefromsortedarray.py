#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int


Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
        """
        len_nums = len(nums)
        if len_nums <= 2:
            return len_nums

        now = 1
        for i in xrange(2, len_nums):
            if nums[i] != nums[now - 1]:
                now += 1
                nums[now] = nums[i]

        # print nums
        if (now + 1) < len_nums:
            del nums[now + 1:]
        print nums
        return now + 1


# nums = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5]
# nums = [1,1,1,2,2,2,3]
nums = [1, 2, 2]
so = Solution()
print so.removeDuplicates(nums)   
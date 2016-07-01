#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160701

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]


Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

这道题的思想是：
先将列表从大到小排序
挨个遍历列表中元素，将当前元素作为第一个元素
使用两个指针指向在当前元素之后的数字
当前元素和后面两个指针指向数字相加
如果和为0，则表示这三个元素满足条件
如果和大于0，则指向末尾的指针应该向数字小的方向移动
如果和小于0，则指向小数字的指针应该向数字增大方向移动

这个方法的时间复杂性是O(n^2):n-2个元素遍历一遍，第二重循环中遍历n个元素
        """

        # 数组从小到大排序
        nums.sort()
        ret = []

        # 获取数组中元素个数
        nums_len = len(nums)
        if not nums_len:
            return []

        # 外层循环，从第一个遍历到第n-2个元素
        for i in xrange(0, nums_len-2):
            # 剩余数字中，指向数字小的指针
            low = i + 1

            # 剩余数字中，指向数字大的指针
            high = nums_len - 1

            # 当low>=high时，则证明剩余数字已经遍历完
            while low < high:
                three = nums[i] + nums[low] + nums[high]

                if three == 0:
                    # 如果三个数字相加为0，满足条件
                    temp = [nums[i], nums[low], nums[high]]
                    if temp not in ret:
                        ret.append(temp)
                    low += 1
                    high -= 1
                elif three > 0:
                    # 三个数字之和大于0，指向大数的指针左移
                    high -= 1
                else:
                    # 三个数字之和小于0，指向小数的指针右移
                    low += 1
        return ret


S = [-1, 0, 1, 2, -1, -4]
so = Solution()
print so.threeSum(S)
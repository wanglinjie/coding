#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160705
import sys

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

Implement next permutation, 
which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, 
it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. 
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

思路：
从最后一个元素向前遍历，如果遇到第i个元素比i-1个元素大，则可以将i-1之后元素排序，寻找比当前
大的最小元素
        """
        nums_len = len(nums)
        if (not nums_len) or (nums_len == 1):
            return
        # 需要变换顺序的数组元素
        temp = []

        # 从数组最后一位向前遍历
        for i in xrange(nums_len-1, -1, -1):
            if i > 0:
                if nums[i] > nums[i-1]:
                    # 如果当前元素比前一个元素大
                    temp.append(nums[i])
                    temp.append(nums[i-1])
                    break
                else:
                    temp.append(nums[i])
            else:
                # 如果已经遍历到数组第一个元素，则证明整个数组逆序
                nums.reverse()
                return
        # a = temp[0]
        # temp.sort()
        # 变换为数组中原有顺序
        temp.reverse()
        temp_len = len(temp)
        # a = temp[0]
        # temp[0] = temp[1]
        # temp[1] = a
        # # temp[1:].sort()
        # temp[1:] = sorted(temp[1:])
        # print temp
        # return temp

        # 找到比temp中第一个元素大的最小元素
        min_max = -1
        for i in xrange(1, temp_len):
            if temp[i] > temp[0]:
                if min_max != -1:
                    if temp[i] < temp[min_max]:
                        min_max = i
                else:
                    min_max = i

        a = temp[0]
        temp[0] = temp[min_max]
        temp[min_max] = a
        # temp数组中后续元素排序
        temp[1:] = sorted(temp[1:])

        nums[nums_len - temp_len:] = temp

nums = [1, 2, 4, 5, 3]
# nums = [1, 2, 4, 3, 2]
# nums = [2, 4, 3]
nums = [1, 2, 3, 4, 5]
so = Solution()
so.nextPermutation(nums)
print nums

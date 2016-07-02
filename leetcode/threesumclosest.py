#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160702
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

Given an array S of n integers, 
find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

这道题的思路和3sum的类似，只是只需记录和target最近的一个和即可

        """
        nums_len = len(nums)
        if nums_len < 3:
            return 0
        # 数组从小到大排序
        nums.sort()
        distance = sys.maxint

        # 遍历数组中元素
        for i in xrange(nums_len-2):
            # 指向小数指针
            low = i + 1
            # 指向大数指针
            high = nums_len - 1

            # 内循环
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                temp = three_sum - target

                # 记录和目标最接近的一个距离
                if abs(temp) < abs(distance):
                    print distance, temp, three_sum
                    distance = temp
                if temp == 0:
                    return target
                elif temp < 0:
                    low += 1
                else:
                    high -= 1
        closest = distance + target
        # print distance, target
        return closest

# S = [0, 1, 2, 3, 1, 2, 0, 0]
# target = 1
S = [0,2,1,-3]
target = 1
so = Solution()
print so.threeSumClosest(S, target)
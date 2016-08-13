#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160813

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Given an unsorted array, 
find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and 
fit in the 32-bit signed integer range.

利用桶排序
        """
        if len(nums)<2:
            return 0
        # 求数组中最大和最下值
        maxV, minV = max(nums), min(nums)
        # 计算数组中最大gap的最小值
        maxGap = (maxV-minV)//(len(nums)-1)
        bSize = maxGap+1
        # 创建桶
        buckets = [[] for _ in range((maxV-minV)//bSize+1)]
        # 将数字放入桶中
        for n in nums:
            # 每个bsize gap内的数字放入一个桶中
            buckets[(n-minV)//bSize].append(n)

        # 去除空的列表
        buckets = [b for b in buckets if b]
        for i in range(1, len(buckets)):
            # 求max gap
            maxGap = max(maxGap, min(buckets[i])-max(buckets[i-1]))
        return maxGap
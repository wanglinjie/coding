#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160826

import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
The algorithm should run in linear time and in O(1) space.

1.排序，之后统计每个数字出现次数
2.使用hash，记录每个数字出现次数


        """

        # linear time, O(n) space
        # if not nums:
        #     return []
        # threshold = (len(nums) / 3)
        # ret = []
        # num_dic = collections.defaultdict(int)
        # for i in nums:
        #     num_dic[i] += 1
        # for i in num_dic:
        #     if num_dic[i] > threshold:
        #         ret.append(i)
        # return ret


        # 下面的是O(1) time, O(1) space
        if not nums:
            return []
        threshold = (len(nums) / 3)
        number1 = ""
        count1 = 0

        number2 = ""
        count2 = 0

        for i in nums:
            if i == number1:
                count1 += 1
            elif i == number2:
                count2 += 1
            elif count1 == 0:
                number1 = i
                count1 = 1
            elif count2 == 0:
                number2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for i in nums:
            if i == number1:
                count1 += 1
            elif i == number2:
                count2 += 1
        ret = []
        if count1 > threshold:
            ret.append(number1)
        if count2 > threshold:
            ret.append(number2)
        return ret


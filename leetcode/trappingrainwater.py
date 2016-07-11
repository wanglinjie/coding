#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160710

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!


思路：
如果当前位置上有存储水，则该位置两侧的高度要比当前位置高度高
所以可以记录当前位置两侧的最高高度
从左向右遍历，记录每个位置左侧最高高度
从右向左遍历，记录每个位置右侧最高高度
然后再遍历一遍，计算当前位置是否有水
最后遍历，统计总的存储水量
        """
        height_len = len(height)
        # 记录每个位置左侧最高高度
        left = [0] * height_len
        # 记录每个位置右侧最高高度
        right = [0] * height_len
        # 记录每个位置可以存储的水量
        store_water = [0] * height_len
        max_height = 0

        # 遍历获取每个位置左侧最高高度
        for i in xrange(height_len):
            left[i] = max_height
            if height[i] > max_height:
                max_height = height[i]

        max_height = 0
        # 遍历获取每个位置右侧最高高度
        for i in xrange(height_len-1, -1, -1):
            right[i] = max_height
            if height[i] > max_height:
                max_height = height[i]

        # 计算每个位置可以存储水量
        for i in xrange(height_len):
            # 获取当前位置两侧最高高度中最低的一个
            temp = min(left[i], right[i])

            if temp > height[i]:
                store_water[i] = temp - height[i]
        ret = 0
        # 计算总的存储水量
        for i in store_water:
            ret += i
        return ret

height = []
so = Solution()
print so.trap(height)


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160829

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int

Given n balloons, indexed from 0 to n-1. Each balloon is 
painted with a number on it represented by array nums. 
You are asked to burst all the balloons. 
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, 
the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. 
They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        print nums
        dp = [[0] * (n+2) for i in xrange(n+2)]
        return self.coins(1, n, dp, nums)


    def coins(self, start, end, dp, nums):
        if dp[start][end] > 0:
            return dp[start][end]
        for x in xrange(start, end+1):
            dp[start][end] = max(dp[start][end], self.coins(start, x-1, dp, nums) + nums[start-1] * nums[x] * nums[end+1] + self.coins(x+1, end, dp, nums))
        return dp[start][end]


nums = [3,1,5,8]
so = Solution()
print so.maxCoins(nums)
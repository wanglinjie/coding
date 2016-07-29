#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160729

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


思路：
动态规划思想，记录当前位置之前的最小值
如果最小值比当前小，则计算利润，并和最大利润比较，如果当前利润大则保存
最小值比当前大，则当前并不会产生什么利润
        """
        prices_num = len(prices)
        if not prices_num:
            return 0
        max_profit = 0
        min_value_left = prices[0]
        for i in xrange(1, prices_num):
            if prices[i] > min_value_left:
                profit = prices[i] - min_value_left
                if profit > max_profit:
                    max_profit = profit
            else:
                min_value_left = prices[i]
        return max_profit
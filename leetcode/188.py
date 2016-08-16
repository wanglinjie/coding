#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160816
import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).


The key function is:
sell[i]=max(sell[i],buy[i]+price)
buy[i]=max(buy[i],sell[i-1]-price)
The first function means that we are now at price, and we are in the ith transaction, and we are gonna ending with a sell, we can either do nothing which refers to sell[i], or we can sell the stock which means we must do buy[i] first and thus refers to buy[i]+price.
The second function works in the similar way, we can either do nothing which refers to buy[i] or we can sell the stock in transaction i-1 first and buy the stock now, which refers to sell[i-1]-price, apparently, we need the max value of the two.
The initial value of buy and sell can be thought as follows:
we init buy to Integer.MIN_VALUE to confirm that it will be updated in the loop because of the Math.max function
we init sell to 0 because we actually has nothing to sell and at first we got 0 money, the result will be our pure profit
the return value is sell[k] which means we end with the sell of the kth transaction
        """
        ret = 0
        prices_len = len(prices)
        # 如果可以操作次数是总价格数的一半以上，则可以将k视为无穷多次
        # 只要遇到比前一天高的就可以进行操作
        if k > (prices_len/2):
            for i in xrange(1, prices_len):
                ret += max(0, prices[i] - prices[i-1])
            return ret
        buy = [-sys.maxint-1] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for i in xrange(1, k+1):
                sell[i] = max(sell[i], buy[i]+price)
                buy[i] = max(buy[i], sell[i-1]-price)
        return sell[k]


prices = [1, 2, 3, 4]
k = 1
so = Solution()
print so.maxProfit(k, prices)
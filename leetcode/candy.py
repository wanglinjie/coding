#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160806

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
        """
        people = len(ratings)
        left = [1] * people
        right = [1] * people

        # 从左向右遍历，如果i元素大于i-1元素，则糖比i-1元素多一个，否则为1
        for i in xrange(1, people):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
        # 从右向左遍历，如果i元素大于i+1元素，则糖比i+1元素多一个，否则为1
        for i in xrange(people-1-1, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        ret = 0
        for i in xrange(people):
            ret += max(left[i], right[i])
        return ret

ratings = [5, 4, 3, 2, 2, 1, 2]
so = Solution()
print so.candy(ratings)
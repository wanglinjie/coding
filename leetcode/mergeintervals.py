# date:20160528
# -*- coding:utf-8 -*-

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
        """
        if not intervals:
            return intervals
        results = []
        intervals = sorted(intervals, cmp=self.interval_comp)
        results.append(intervals[0])
        for i in xrange(1, len(intervals)):
            if results[-1].end >= intervals[i].start:
                results[-1].end = max(results[-1].end, intervals[i].end)
            else:
                results.append(intervals[i])
        return results



    def interval_comp(self, a, b):
        '''
        对节点进行比较
        '''
        if a.start == b.start:
            return a.end - b.end
        return a.start - b.start


inter = Interval(1, 2)
so = Solution()
so.merge([inter])
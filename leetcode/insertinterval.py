# date:20160528
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
        """
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        # if newInterval.end < intervals[0].start:
        #     return intervals.insert(0, newInterval)
        results = []
        intervals_num = len(intervals)
        for i in xrange(intervals_num):
            if newInterval.start <= intervals[i].end:
                if newInterval.end < intervals[i].start:
                    results.append(newInterval)
                    results.extend(intervals[i:])
                    return results
                tempInterval = Interval()
                tempInterval.start = min(intervals[i].start, newInterval.start)
                # find_end = False
                j = 0
                for j in xrange(i, intervals_num):
                    if (intervals[j].end >= newInterval.end):
                        tempInterval.end = intervals[j].end
                        break

                    if (j + 1) == intervals_num:
                        tempInterval.end = max(intervals[j].end, newInterval.end)
                        break

                    if (intervals[j+1].start > newInterval.end):
                        tempInterval.end = max(intervals[j].end, newInterval.end)
                        break

                results.append(tempInterval)
                if (j + 1) < intervals_num:
                    results.extend(intervals[j+1:])
                break
            else:
                results.append(intervals[i])
                if (i + 1) == intervals_num:
                    results.append(newInterval)

        return results



so = Solution()
so.insert()
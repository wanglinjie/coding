#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160810

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
Given n points on a 2D plane, 
find the maximum number of points that lie on the same straight line.

思路：
一条直线可以看作为y=kx+b
通过(k, b)来定位一条直线，只需记录两点之间连线斜率和偏移量
如果k，b相等则证明点在同一条直线上
        """
        d = collections.defaultdict(list)
        for i in range(1, len(points)):
            for j in range(i):
                p1, p2 = points[i], points[j]
                if p1.x == p2.x:
                    t = (float('inf'), p1.x)
                else:
                    t = ((p1.y-p2.y)/float(p1.x-p2.x), (p1.x*p2.y-p2.x*p1.y)/float(p1.x-p2.x))
                d[t] += [p1, p2]
        return max(len(set(l)) for l in d.values()) if len(points)>1 else len(points)
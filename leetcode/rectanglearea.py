#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160618

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
        """
        x_left = max(A, E)
        x_right = min(C, G)
        y_up = min(D, H)
        y_down = max(B, F)
        repeat_area = (x_right-x_left) * (y_up-y_down)
        if (x_right < A) or (x_right < E):
            repeat_area = 0
        elif (x_left > C) or (x_left > G):
            repeat_area = 0
        elif (y_up < B) or (y_up < F):
            repeat_area = 0
        elif (y_down > D) or (y_down > H):
            repeat_area = 0
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        return area1 + area2 - repeat_area
A = 0
B = 0
C = -2
D = -2
E = 2
F = -2
G = 5
H = 5

so = Solution()
print so.computeArea(A, B, C, D, E, F, G, H)
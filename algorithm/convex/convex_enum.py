#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
求解凸包问题
'''
from __future__ import division
import random as ran
import cPickle
import time
import copy

import numpy as np
import matplotlib.pyplot as plt

def in_triangle(pointa, pointb, pointc, pointd):
    '''
    cite:http://www.cnblogs.com/graphics/archive/2010/08/05/1793393.html
    v0 = pointc – pointa, v1 = pointb – pointa, v2 = pointd – pointa，则v2 = u * v0 + v * v1
    u = ((v1•v1)(v2•v0)-(v1•v0)(v2•v1)) / ((v0•v0)(v1•v1) - (v0•v1)(v1•v0))
    v = ((v0•v0)(v2•v1)-(v0•v1)(v2•v0)) / ((v0•v0)(v1•v1) - (v0•v1)(v1•v0))
    '''
    v0 = pointc - pointa
    v1 = pointb - pointa
    v2 = pointd - pointa
    # print v0, v1, v2

    v00 = np.dot(v0, v0)
    v01 = np.dot(v0, v1)
    v02 = np.dot(v0, v2)
    v11 = np.dot(v1, v1)
    v12 = np.dot(v1, v2)
    # print v00, v01, v02, v11, v12
    try:
        den = 1 / (v00 * v11 - v01 * v01)
    except:
        #print "in except"
        return False

    u = (v11 * v02 - v01 * v12) * den
    if (u < 0) or (u > 1):
        #print "u", u
        return False

    v = (v00 * v12 - v01 * v02) * den
    if (v < 0) or (v > 1):
        #print "v", v
        return False

    if u + v <= 1:
        return True
    else:
        #print "u+v", u+v
        return False


class Convex_enum(object):
    '''
    '''
    def __init__(self, n):
        '''
        type: n: int
        param: n: the number of the point
        '''
        self.n = n
        self.points = []

    def gen_random(self):
        '''
        随机生成n个点
        '''
        points = []
        for i in xrange(self.n):
            x = ran.uniform(0, 100)
            y = ran.uniform(0, 100)
            temp_point = np.asarray([x, y])
            points.append(temp_point)
        # with open("points.txt", 'w') as f:
        #     cPickle.dump(points, f)
        self.points = copy.deepcopy(points)
        return points

    def convex_points(self):
        del_points = []
        points = self.gen_random()
        for i in xrange(self.n):
            if i in del_points:
                continue
            for j in xrange(self.n):
                if j in del_points:
                    continue
                for k in xrange(self.n):
                    if k in del_points:
                        continue
                    for d in xrange(self.n):
                        if d in del_points:
                            continue
                        if (i == j) or (i == k) or (i == d) or (j == k) or (j == d) or (k == d):
                            continue
                        if in_triangle(points[i], points[j], points[k], points[d]):
                            del_points.append(d)

        output_points = []
        for i in xrange(self.n):
            if i not in del_points:
                output_points.append(points[i])
        return output_points 


def print_point(points):
    points_sort = sorted(points, key=lambda point: point[0])
    left = points_sort[0]
    right = points_sort[-1]
    del points_sort[0]
    del points_sort[-1]


    # the line is y = ax + b
    a = (right[1] - left[1]) / (right[0] - left[0])
    b = left[1] - a * left[0]

    up_points = []
    down_points = []
    for i in points_sort:
        if i[1] - (a * i[0] + b) < 0:
            down_points.append(i)
        else:
            up_points.append(i)
    output = []
    output.append(left)
    output = output + down_points
    output.append(right)
    output = output + sorted(up_points, key=lambda point: point[0], reverse=True)
    return output



if __name__ == "__main__":
    number = int(raw_input("Please input the number of the points:"))
    # numbers = [200, 400, 600, 800, 1000]
    # number = 100

    convex = Convex_enum(number)

    t0 = time.clock()
    output_points = convex.convex_points()
    print time.clock() - t0

    # with open('result_enum.txt', 'w') as f:
    #     for i, j in output_points:
    #         f.write(str(i) + ' ')
    #         f.write(str(j) + '\n')
    sortp = []
    for i in output_points:
        sortp.append(tuple(i))

    sort_points = print_point(sortp)
    x1 = []
    y1 = []
    for i in sort_points:
        xi, yi = i
        x1.append(xi)
        y1.append(yi)
    x1.append(x1[0])
    y1.append(y1[0])

    x2 = []
    y2 = []
    for i in convex.points:
        xi, yi = i
        x2.append(xi)
        y2.append(yi)

    plot1 = plt.plot(x1, y1)
    plot2 = plt.plot(x2, y2, 'o')
    
    plt.legend([plot1, plot2], ('convex point', 'points'))
    plt.show()

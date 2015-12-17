#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
使用Graham-scan来求解凸包问题
'''

from __future__ import division
import random as ran
import cPickle
import time
import matplotlib.pyplot as plt

import numpy as np

class Convex_graham(object):
    '''
    '''
    def __init__(self, n):
        self.origin = 0
        self.n = n
        self.points = []
        self.origin_point = None

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
        self.points = points
        # with open("points.txt", 'r') as f:
        #     points = cPickle.load(f)
        # self.points = points
        # print points

    def get_origin_point(self):
        '''
        返回y值最小的点
        '''
        origin = 0
        min_y = 1000
        for i in xrange(self.n):
            _, y = self.points[i]
            if y < min_y:
                min_y = y
                origin = i
        self.origin = origin
        self.origin_point = self.points[origin]
        # print self.origin_point

    def get_angle(self, pointb):
        '''
        type: pointb: numpy.ndarray
        param: pointb: the other pointc - the origin point

        返回值：返回点与原点夹角的cos值
        '''
        temp_point = np.asarray((1, 0))
        x, y = pointb
        abvalue = (x ** 2 + y ** 2) ** 0.5
        cosvalue = np.dot(pointb, temp_point) / abvalue
        return cosvalue


    def sort_angle(self):
        '''
        将点按照与原点的极角从小到大排序，即cos值从大到小排序
        返回的是排好序的点的在points中的位置
        '''
        cosvalues = {}
        # origin_point = self.points[self.origin]
        for i in xrange(self.n):
            if i != self.origin:
                cosvalue = self.get_angle(self.points[i] - self.origin_point)
                if cosvalue in cosvalues:
                    num = cosvalues[cosvalue]
                    if self.points[num][1] > self.points[i][1]:
                        print "del ", self.points[i]
                        del self.points[i]
                    else:
                        print "del ", self.points[num] 
                        del self.points[num]
                        cosvalues[cosvalue] = i
                    self.n = self.n - 1
                else:
                    cosvalues[cosvalue] = i
        sorted_cosvalues = sorted(cosvalues.items() , reverse=True)
        # 去除极角相同的点
        # print sorted_cosvalues
        return [value for key, value in sorted_cosvalues]

    def left(self, pointa, pointb, pointc):
        '''
        判断是否左转
        '''

        uxb, uyb = pointb - pointa
        uxc, uyc = pointc - pointa
        return uxb*uyc - uxc*uyb

    def graham(self):
        self.gen_random()
        self.get_origin_point()

        convex_points = []
        sorted_cosvalues = self.sort_angle()
        convex_points.append(self.origin)
        convex_points.append(sorted_cosvalues[0])
        convex_points.append(sorted_cosvalues[1])
        # print sorted_cosvalues
        for i in sorted_cosvalues[2:]:
            # convex_points.append(i)
            while self.left(self.points[convex_points[-2]], self.points[convex_points[-1]], self.points[i]) < 0:
                convex_points.pop()
                # print i
            convex_points.append(i)
        return convex_points
    




if __name__ == "__main__":
    number = int(raw_input("输入点的个数:"))
    # numbers = [1000, 2000, 3000, 4000, 5000]
    # for number in numbers:
    convex = Convex_graham(number)
    t0 = time.clock()
    convex_points = convex.graham()
    total_time = time.clock() - t0
    print total_time

    x = []
    y = []
    with open('result_graham_partition.txt', 'w') as f:
        for i in convex_points:
            xi, yi = convex.points[i]
            x.append(xi)
            y.append(yi)
            f.write(str(xi) + ' ')
            f.write(str(yi) + '\n')
    x.append(x[0])
    y.append(y[0])

    x2 = []
    y2 = []
    for i in convex.points:
        xi, yi = i
        x2.append(xi)
        y2.append(yi)

       
    plot1 = plt.plot(x, y)
    plot2 = plt.plot(x2, y2, 'o')
    
    plt.legend([plot1, plot2], ('convex point', 'points'))
    plt.show()

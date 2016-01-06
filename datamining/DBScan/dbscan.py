#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
DBScan聚类算法
@author:    Wanglj
@date:  2015.12.11
'''

import re

import numpy as np
import matplotlib.pylab as plt

class Data(object):
    '''
    处理数据，比如导入数据
    '''
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        '''
        从文件中读取数据
        '''
        records = []
        with open(self.filename, 'r') as f:
            for line in f:
                record = line.split(',')
                frecord = map(float, record[:])
            
                records.append(list(frecord))
        self.data = np.asarray(records)

        return self.data

class DBScan(object):
    '''
    dbscan
    '''
    def __init__(self, eps, Minpts, filename):
        self.eps = eps
        self.Minpts = Minpts
        self.da = Data(filename)
        self.data = self.da.load_data()

        # 噪音点
        self.noise = []

        # 频繁点
        self.density_points = []
        self.density_labels = []

        # 边界点
        self.border_points = []
        self.border_labels = []


    def geteps_point(self, pointA):
        '''
        获得距点pointA距离在eps内的点
        '''
        points = []
        for i in xrange(np.shape(dbscan.data)[0]):
            point = self.data[i]
            if np.sum((self.data[pointA] - point)**2)**0.5 <= self.eps:
                points.append(i)     
        return points


    def cluster(self):
        cluster_num = 0
        # 访问过的点
        visited_points = []
        

        # 入栈遍历点
        scan_points = []

        for i in xrange(np.shape(dbscan.data)[0]):
            if i in visited_points:
                continue
         
            scan_points.append(i)

            while scan_points:
                if scan_points[0] in visited_points:
                    del scan_points[0]
                    continue
                visited_points.append(scan_points[0])
                points = self.geteps_point(scan_points[0])

                if len(points) >= self.Minpts:
                    self.density_points.append(scan_points[0])
                    self.density_labels.append(cluster_num)
                    for border_i in points:
                        scan_points.append(border_i)
                else:
                    # 边界点
                    label = -1
                    for border_i in points:
                        if border_i in self.density_points:
                            label = self.density_labels[self.density_points.index(border_i)]
                            break
                    if label > -1:
                        self.border_points.append(scan_points[0])
                        self.border_labels.append(label)
                del scan_points[0]

            if cluster_num in self.density_labels:

                cluster_num += 1

        # 查找噪音点
        for i in xrange(np.shape(dbscan.data)[0]):
            if (i not in self.density_points) and (i not in self.border_points):
                points = self.geteps_point(i)
                label = -1
                for noisei in points:
                    if noisei in self.density_points:
                        label = self.density_labels[self.density_points.index(noisei)]
                        self.border_points.append(point)
                        self.border_labels.append(label)
                        break
                if label > -1:
                    self.noise.append(point)



if __name__ == "__main__":
    eps = 3
    Minpts = 2
    filename = "data.txt"
    dbscan = DBScan(eps, Minpts, filename)
    dbscan.cluster()

    print np.shape(dbscan.data)
    print len(dbscan.data)


    print dbscan.density_labels
    max_num = max(dbscan.density_labels)
    for i in xrange(max_num + 1):
        points_index = [label == i for label in dbscan.density_labels]

        points = []
        for j in xrange(len(points_index)):
            if points_index[j]:
                points.append(dbscan.data[dbscan.density_points[j]])
        x = []
        y = []
        for point in points:
            xi, yi = point
            x.append(xi)
            y.append(yi)
        plt.plot(x, y, 'o')
        plt.hold(True)

    print len(dbscan.density_points)
    print len(dbscan.border_points)
    print len(dbscan.noise)
    plt.show()
            
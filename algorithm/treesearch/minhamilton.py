#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
分支界限法求解最小哈密顿环
'''
import random as ran
from copy import deepcopy
import time

import numpy as np


bignum = 1000000

class Graph(object):
    '''
    '''
    def __init__(self, n):
        self.n = n

        self.asjmatrix = np.zeros((n, n))

    def gen_graph(self):
        '''
        随机形成一个图
        '''
        for i in xrange(self.n):
            for j in xrange(i+1, self.n):
                self.asjmatrix[i, j] = self.asjmatrix[j, i] = ran.randint(1, 20)
            self.asjmatrix[i, i] = bignum

        # print self.asjmatrix
        # print np.argmin(self.asjmatrix)

class Node(object):
    '''
    搜索树中每个节点
    '''
    def __init__(self, edge, cost, father):
        '''
        edge是这个点所代表的边
        cost是加入这个边之后这条路径的代价
        '''
        self.edge = edge
        self.cost = cost

        # 左孩子
        self.left_child = None
        # 右孩子
        self.right_child = None
        # 父亲节点 
        self.father = father


class Hamilton(Graph):
    '''
    '''
    def __init__(self, n):
        super(Hamilton, self).__init__(n)
        # 当前搜索中哈密顿环的最小值
        self.minvalue = 100000

        self.searchtree = []

        # self.newmatrix = copy.deepcopy(self.asjmatrix)

    def change_matrix(self, newmatrix):
        '''
        newmatrix需要时deep copy
        '''
        min_cost = 0

        label = np.argmin(newmatrix, axis=1)
        # print label
        for i in xrange(self.n):
            if newmatrix[i, label[i]] != 0:
                if newmatrix[i, label[i]] == bignum:
                    continue
                min_cost = min_cost + newmatrix[i, label[i]]
                newmatrix[i] = newmatrix[i] - newmatrix[i, label[i]]
                

        label = np.argmin(newmatrix, axis=0)
        for i in xrange(self.n):
            if newmatrix[label[i], i] != 0:
                if newmatrix[label[i], i] == bignum:
                    continue
                min_cost = min_cost + newmatrix[label[i], i]
                newmatrix[:, i] = newmatrix[:, i] - newmatrix[label[i], i]
                
        return min_cost, newmatrix

    def child_change_matrix(self, newmatrix, x, y, drop):
        '''
        newmatrix是deep copy
        '''
        if not drop:
            newmatrix[x] = bignum
            newmatrix[:, y] = bignum
            newmatrix[y, x] = bignum
        else:
            newmatrix[x, y] = bignum

        return newmatrix



    def get_max_cost(self, graph_matrix):
        '''
        查找代价最大的点
        '''
        max_cost = 0
        x = y = 0
        for i in xrange(self.n):
            for j in xrange(self.n):
                if graph_matrix[i, j] == 0:
                    # 避免查找最小值时返回该零点
                    graph_matrix[i, j] = bignum
                    x_min = np.argmin(graph_matrix[i])
                    y_min = np.argmin(graph_matrix[:, j])
                    cost = graph_matrix[i, x_min] + graph_matrix[y_min, j]
                    if cost >= max_cost:
                        max_cost = cost
                        x = i
                        y = j
                    # else:
                        # print graph_matrix[i, x_min]
                        # print "cost", cost, max_cost
                    graph_matrix[i, j] = 0

        return x, y, max_cost

    def find_edges(self, node, cost):
        temp = [0] * self.n
        search_list = []
        while True:
            if isinstance(node, Node):
                if node.edge != ():
                    search_list.append(node.edge)
                node = node.father
            else:
                break
        
        search_keys = dict(search_list)
        # print search_keys
        list1 = []
        list1.append(0)
        while True:
            next_num = search_keys[list1[-1]]
            if next_num != list1[0]:
                list1.append(next_num)
            else:
                break
        if len(list1) == self.n:
            self.minvalue = cost
            self.searchtree = search_list

        

        # print list1
        # raise TypeError
        # if len(list1) == self.n:
        #     self.minvalue = cost
        #     self.searchtree = search_list
        # else:
        #     print list1
        #     print "not correct"
        #     raise TypeError


        # if cost < self.minvalue:
        #     self.minvalue = cost
        #     self.searchtree = search_list

    def find_path(self, graph_matrix, father_node, cost, points_num):
        '''
        node为该节点
        graph_matrix为deep copy
        '''
        if cost >= self.minvalue:
            # 舍弃该节点
            return

        if points_num == self.n:
            # 判断是否构成一个环
            # if isacycle:
            #     return 
            # else:
            #     return
            # self.minvalue = cost
            self.find_edges(father_node, cost)
            return

        x, y, max_cost = self.get_max_cost(graph_matrix)
        # print "max_cost", cost, max_cost
        # return

        # 左孩子
        left_child_matrix = self.child_change_matrix(deepcopy(graph_matrix), x, y, False)
        left_min_cost, _ = self.change_matrix(left_child_matrix)
        left_child = Node((x, y), cost + left_min_cost, father_node)
        self.find_path(left_child_matrix, left_child, cost + left_min_cost, points_num + 1)

        # 右孩子
        # print "right"

        right_child_matrix = self.child_change_matrix(deepcopy(graph_matrix), x, y, True)
        right_min_cost, _ = self.change_matrix(right_child_matrix)
        right_child = Node((), cost + max_cost, father_node)
        # print cost, self.minvalue, max_cost, right_min_cost
        self.find_path(right_child_matrix, right_child, cost + max_cost + right_min_cost, points_num)




    def search_tree(self):
        '''
        分之界限开始函数
        '''
        self.gen_graph()

        min_cost, newmatrix = self.change_matrix(deepcopy(self.asjmatrix))
        root = Node((), min_cost, None)
        self.find_path(deepcopy(newmatrix), root, min_cost, 0)

        # print self.asjmatrix
        # print self.minvalue
        # print self.searchtree


        search_keys = dict(self.searchtree)
        list1 = []
        list1.append(0)
        iter_num = 0
        while True:
            next_num = search_keys[list1[-1]]
            if next_num != list1[0]:
                list1.append(next_num)
            else:
                break
            # iter_num = iter_num + 1
            # if iter_num > self.n:
            #     break

        # if len(list1) == self.n:
        #     print "right"
        #     # print list1
        # else:
        #     print list1

def main():
    # number = int(raw_input("Please input the number:"))
    numbers = [8, 10, 12, 14, 16, 18, 20]
    for number in numbers:
        hamil = Hamilton(number)
    # hamil.change_matrix()
        t0 = time.clock()
        hamil.search_tree()
        total_time = time.clock() - t0
        print total_time

if __name__ == "__main__":
    main()
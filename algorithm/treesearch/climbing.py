#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
爬山法求解求解哈密顿环
优先选取度小的
'''
import random as ran
import time

import numpy as np

class Graph(object):
    '''
    '''
    def __init__(self, n):
        '''
        n为图中顶点的个数
        '''
        self.n = n
        self.asjmatrix = np.zeros((n, n))
        # self.pathmatrix = np.zeros((n, n))
        self.search_tree = {}
        self.search_tree[0] = {}
        self.search_list = [0]

        self.point_degree = []

    def gen_graph(self):
        '''
        随机形成一个图
        现在效果还不好，接下来需要改善
        '''
        for i in xrange(self.n):
            for j in xrange(i+1, self.n):
                self.asjmatrix[i, j] = self.asjmatrix[j, i] = ran.randint(0, 1)

    def find_path(self, tree, depth):
        if depth == len(self.search_list):
            return tree.keys()
        if isinstance(tree, dict):
            temp_tree = tree[self.search_list[depth]]
            # print "hello world"
            return self.find_path(temp_tree, depth + 1)

    def get_degree(self):
        for i in xrange(self.n):
            num = 0
            for j in xrange(self.n):
                if self.asjmatrix[i, j]:
                    num = num + 1
            self.point_degree.append(num)

    def find_next(self):
        '''
        图搜索中下一个点
        '''
        min_degree = 1000
        min_point = 0
        last_point = self.search_list[-1]
        for i in xrange(self.n):
            # 当前节点到节点i有连通
            if self.asjmatrix[last_point, i]:
                # 该路径没有遍历过
                path = self.find_path(self.search_tree, 0)
                if i in path:
                    continue
                else:
                    if i != 0:
                        if i not in self.search_list:
                            degree = self.point_degree[i]
                            if degree < min_degree:
                                min_degree = degree
                                min_point = i
                    else:
                        if len(self.search_list) == self.n:
                            return 0
        if min_degree < 1000:
            return min_point
        else:
            return -1

    def add_node(self, tree, depth, point):
        if depth == len(self.search_list):
            tree[point] = {}
            return
        if isinstance(tree, dict):
            temp_tree = tree[self.search_list[depth]]
            self.add_node(temp_tree, depth+1, point)


    def dfs(self):
        '''
        深度优先搜索
        '''
        while True:
            next_point = self.find_next()
            if next_point != -1:
                self.add_node(self.search_tree, 0, next_point)
                self.search_list.append(next_point)
            else:
                if len(self.search_list) == 1:
                    return False
                else:
                    self.search_list.pop()
                # 增加这条搜索路径不行
            if len(self.search_list) == self.n + 1:
                print self.search_list
                return True
                # return search_list

def test():
    tree = {}
    tree[0] = {}
    for i in tree:
        for j in tree[i]:
            for k in xrange(3):
                i[k] = {}
    print tree

def main():
    iter_num = [8, 10, 12, 14, 16, 18, 20]
    f = open("timd_cli.txt", "w+")
    for n in iter_num:
        graph = Graph(n)
        graph.gen_graph()
        graph.get_degree()
        t0 = time.clock()
        if graph.dfs():
            print "yes"
        else:
            print "flase"
        total_time = time.clock() - t0
        f.write(str(n) + " " + str(total_time) + "\n")

    print graph.asjmatrix

def test():
    n = int(raw_input("Please input the number of the points:"))
    graph = Graph(n)
    graph.gen_graph()
    graph.get_degree()
    if graph.dfs():
        print "yes"
    else:
        print "flase"
    print graph.asjmatrix

if __name__ == "__main__":
    main()
    # test()
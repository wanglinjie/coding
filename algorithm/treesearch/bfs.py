#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
求解哈密顿环
'''
import random as ran
import copy
import time

import numpy as np

class Node(object):
    '''
    搜索树中的每个节点
    '''
    def __init__(self, node_name, search_list):
        '''
        search_list是从根到当前节点的搜索路径(深拷贝)
        '''
        self.node_name = node_name
        self.search_list = copy.deepcopy(search_list)
        self.search_list.append(node_name)
        # 记录孩子节点，可以是多个孩子节点
        # self.child = []
        # self.father = father

class Graph(object):
    '''
    图
    '''
    def __init__(self, n):
        self.n = n
        self.asjmatrix = np.zeros((n, n))
        # self.asjmatrix = np.ones((n, n))

    def gen_graph(self):
        '''
        随机形成一个图
        '''
        for i in xrange(self.n):
            for j in xrange(i+1, self.n):
                # 两点之间的值为1代表有边连接
                self.asjmatrix[i, j] = self.asjmatrix[j, i] = ran.randint(0, 1)

class Hamilton(Graph):
    '''
    求解哈密顿环类
    '''
    def __init__(self, n):
        '''
        n为图中顶点的个数
        '''
        super(Hamilton, self).__init__(n)
        # 为广度优先遍历树的节点顺序
        self.search_tree = []
        

    def find_child(self, now_node):
        '''
        图搜索中孩子节点
        '''
        child_nodes = []
        list1 = self.asjmatrix[now_node]
        for i in xrange(self.n):
            if list1[i]:
                child_nodes.append(i)
        return child_nodes

    def bfs(self):
        '''
        广度优先搜索
        '''
        # 根节点
        # root = Node(0, [], None)
        root = Node(0, [])
        self.search_tree.append(root)

        depth = 1
        while self.search_tree:
            now_node = self.search_tree[0]
            # print now_node.node_name
            childs_num = self.find_child(now_node.node_name)
            # print childs_num
            for i in childs_num:
                if i in now_node.search_list:
                    if (len(now_node.search_list) == self.n) and (i == 0):
                        return now_node
                else:
                    child_node = Node(i, now_node.search_list)
                    # 将节点添加为当前拓展节点的孩子
                    # now_node.child.append(child_node)

                    self.search_tree.append(child_node)
            # print "now node ", now_node.node_name, now_node.search_list
            del self.search_tree[0]
        return False

def test():
    n = int(raw_input("Please input the number of the points:"))
    ha = Hamilton(n)
    ha.gen_graph()
    result = ha.bfs()
    if result:
        print result.search_list
    else:
        print "don't have a Hamilton"
    print ha.asjmatrix

def main():
    iter_num = [8, 10, 12, 14]
    f = open("timd_bfs.txt", "w+")
    for n in iter_num:
        ha = Hamilton(n)
        t0 = time.clock()
        ha.gen_graph()
        result = ha.bfs()
        total_time = time.clock() - t0
        if result:
            print result.search_list
        else:
            print "don't have a Hamilton"
        f.write(str(n)+" "+str(total_time)+"\n")
    print ha.asjmatrix

if __name__ == "__main__":
    main()
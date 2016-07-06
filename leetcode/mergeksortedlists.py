#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160705

import sys
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MinHeap(object):
    def __init__(self):
        self.data = [0]
    
    def push(self, x):
        self.data.append(x)
        self.percolateUp(len(self.data)-1)
    
    def pop(self):
        res = self.data[1]
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        self.data.pop()
        self.percolateDown(1)
        return res
    
    def percolateUp(self, idx):
        while idx > 1:
            pa = idx / 2
            if self.data[pa][0] > self.data[idx][0]:
                self.data[pa], self.data[idx] = self.data[idx], self.data[pa]
            idx = pa
            
    def percolateDown(self, idx):
        while 2 * idx < len(self.data):
            child = 2 * idx
            if 2 * idx + 1 < len(self.data) and self.data[2*idx+1][0] < self.data[2*idx][0]:
                child = 2 * idx + 1
            if self.data[idx][0] > self.data[child][0]:
                self.data[child], self.data[idx] = self.data[idx], self.data[child]
            idx = child

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.
        """

        h = MinHeap()
        for l in lists:
            if l: h.push((l.val, l))
        superhead = ListNode(0)
        spt = superhead
        while len(h.data) > 1:
            node = h.pop()[1]
            if node.next: h.push((node.next.val, node.next))
            spt.next = node
            spt = spt.next
        
        return superhead.next

        # 遍历查找值最小的节点

        # 记录各个列表头结点
        # if not lists:
        #     return None
        # topK = []
        # head = None
        # min_index = 0
        # min_val = sys.maxint
        # for i in xrange(len(lists)):
        #     if lists[i].val < min_val:
        #         min_index = i
        #         min_val = lists[i].val
        #     # 初始化存储列表头结点
        #     topK.append(lists[i])

        # # 获取排序后列表头结点
        # head = lists[min_index]
        # now = head
        # if head.next:
        #     # 替换为当前列表下一个节点
        #     topK[min_index] = head.next
        # else:
        #     del topK[min_index]
        # while True:
        #     topK_len = len(topK)
        #     if not topK_len:
        #         # 所有列表都已经排序
        #         break
        #     min_index = 0
        #     min_val = sys.maxint

        #     # 寻找各个列表头结点值最小的节点
        #     for i in xrange(topK_len):
        #         if topK[i].val < min_val:
        #             min_index = i
        #             min_val = topK[i].val

        #     now.next = topK[min_index]
        #     now = now.next
        #     if now.next:
        #         topK[min_index] = now.next
        #     else:
        #         del topK[min_index]
        # return head

nums = [[1, 3], [2, 4, 6], [5]]
lists = []
for i in nums:
    head = None
    for j in xrange(len(i)):
        temp = ListNode(i[j])
        if j > 0:
            head.next = temp
            head = head.next
        else:
            head = temp
            lists.append(head)


so = Solution()
ret = so.mergeKLists(lists)
now = ret
while now:
    print now.val
    now = now.next
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160807

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode

A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
        """
        if not head:
            return head
        # 使用hash记录每个节点出现的位置
        old_node_dic = {}
        # 新节点列表
        new_node_list = []
        i = 0
        node = head
        # 遍历旧链表
        while node:
            # 创建新节点
            new_node = RandomListNode(node.label)
            # 添加新节点
            new_node_list.append(new_node)
            # 记录旧节点位置
            old_node_dic[node] = i
            node = node.next
            i += 1
        node_num = len(new_node_list)
        node = head
        i = 0
        while node:
            # 如果旧节点的random不为None
            if node.random:
                # 获取node的random节点所在位置
                position = old_node_dic[node.random]
                # 将新节点链表的random指向为random位置节点
                new_node_list[i].random = new_node_list[position]
            if i < node_num - 1:
                # 串连新链表
                new_node_list[i].next = new_node_list[i+1]
            i += 1
            node = node.next
        return new_node_list[0]
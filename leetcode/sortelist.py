#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
Sort a linked list in O(n log n) time using constant space complexity.
        """

        # 方法1，读取链表中的值，对值排序后重新写入列表
        # 如果按照只能使用固定空间，这个方法就不符合要求
        # 但是也是一种思想
        if not head:
            return head
        list_values = []
        tempnode = head
        while tempnode:
            list_values.append(tempnode.val)
            tempnode = tempnode.next
        list_values.sort()
        i = 0
        tempnode = head
        while i < len(list_values):
            tempnode.val = list_values[i]
            i += 1
            tempnode = tempnode.next
        return head




#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160609

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

就是合并两个排好序的列表
        """
        if not l1:
            return l2
        if not l2:
            return l1
        ret_head = None
        ret_tail = None
        if l1.val < l2.val:
            ret_head = l1
            ret_tail = l1
            l1 = l1.next
        else:
            ret_head = l2
            ret_tail = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val < l2.val:
                ret_tail.next = l1
                l1 = l1.next
            else:
                ret_tail.next = l2
                l2 = l2.next
            ret_tail = ret_tail.next

        if l1:
            ret_tail.next = l1
        if l2:
            ret_tail.next = l2
        return ret_head

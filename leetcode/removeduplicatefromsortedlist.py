#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode


Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
        """
        if not head:
            return head
        first = head
        second = head
        father = head
        while second:
            if second.next and (second.val == second.next.val):
                while second.next and (second.val == second.next.val):
                    second = second.next
                second = second.next
            else:
                first.val = second.val
                father = first
                first = first.next
                second = second.next
        if father == first:
            return None
        else:
            father.next = None
            return head



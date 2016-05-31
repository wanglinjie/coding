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

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
        """
        now = head
        while now and now.next:
            while now.next and (now.val == now.next.val):
                now.next = now.next.next
            now = now.next
        return head
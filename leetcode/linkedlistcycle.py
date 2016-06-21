#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160621

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
        """
        if not head:
            return False
        first = head.next
        second = head
        while first:
            if first == second:
                return True
            second = second.next
            if first.next:
                first = first.next.next
            else:
                return False
        return False

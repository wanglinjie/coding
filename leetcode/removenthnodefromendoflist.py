#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160609

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

这道题目可以使用两个指针，一个指针先向前移动n步，然后两个指针一起移动，这样可以保证两个指针之间相差n个

为了方便删除节点，可以让第一个指针向前移动n+1步。但是需要注意当删除的节点就是列表第一个节点的情况


        """
        if (not head) or (not n):
            return head
        first = head.next
        second = head
        m = n
        while m and first:
            first = first.next
            m -= 1
        # 如果删除的节点就是第一个节点
        if m == 1:
            return head.next
        while first:
            first = first.next
            second = second.next
        # 删除节点
        second.next = second.next.next
        return head

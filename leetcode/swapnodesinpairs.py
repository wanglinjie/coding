#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160625

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. 
You may not modify the values in the list, only nodes itself can be changed.

基本思想两个节点一组，两个两个交换顺序
使用四个指针，一个指针指向上一组最后一个节点（为了使上一节点能连接到现在这组的节点）
两个指针指向交换当前两个节点
还有一个指针指向下一组的开始节点
        """
        if (not head) or (not head.next):
            return head
        ret_head = head.next
        second = head
        first = head.next
        now = head.next.next
        last = None
        while now and now.next:
            # second.next = first.next
            first.next = second
            if last:
                last.next = first
            last = second

            first = now.next
            second = now
            now = now.next.next
        first.next = second
        second.next = now
        if last:
            last.next = first
        return ret_head

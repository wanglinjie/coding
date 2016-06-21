#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160621

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.


Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
        """
        if (not head) or (not head.next):
            return head
        list_num = 0
        now = head
        while now:
            list_num += 1
            now = now.next
        # print list_num
        middle = list_num / 2
        left_head = head

        right = head
        num = middle-1
        # print num
        # return head
        while num:
            right = right.next
            num -= 1
        temp = right.next
        right.next = None
        right = temp
        # print right.val
        # return head

        # 反向右侧列表
        first = right
        second = right.next
        while second:
            temp = second.next
            second.next = first
            if first.next == second:
                first.next = None
            first = second
            second = temp
        right_head = first

        first = left_head
        second = right_head
        num = 1
        while first:
            if num:
                # print first.val
                temp = first.next
                first.next = second
                first = temp
            else:
                # print second.val
                temp = second.next
                second.next = first
                second = temp
            num += 1
            num %= 2


        # print first.val
        return head


nodes = [1]
root = ListNode(nodes[0])
now = root
for i in nodes[1:]:
    temp = ListNode(i)
    now.next = temp
    now = now.next

so = Solution()

ret = so.reorderList(root)
now = ret
while now:
    print now.val
    now = now.next  
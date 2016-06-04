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
        # if not head:
        #     return head
        # list_values = []
        # tempnode = head
        # while tempnode:
        #     list_values.append(tempnode.val)
        #     tempnode = tempnode.next
        # list_values.sort()
        # i = 0
        # tempnode = head
        # while i < len(list_values):
        #     tempnode.val = list_values[i]
        #     i += 1
        #     tempnode = tempnode.next
        # return head


        # 方法2，使用归并排序，不申请n个空间
        if (not head) or (not head.next):
            return head
        ListNode fast = head
        ListNode slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None

        left = sortList(head)
        right = sortList(fast)
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        elif not right:
            return left
        elif (not left) and (not right):
            return None

        ret = None
        if left.val < right.val:
            ret = left
            left = left.next
        else:
            ret = right
            right = right.next
        now = ret
        while left and right:
            if left.val < right.val:
                now.next = left
                left = left.next
            else:
                now.next = right
                right = right.next
            now = now.next
        return ret

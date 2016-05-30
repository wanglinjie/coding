# -*- coding:utf-8 -*-
# date:20160529

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode


Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
        """
        if (not head) or (k <= 0):
            return head

        first = head
        node_num = 1
        while first.next:
            node_num += 1
            first = first.next
        # 注意当k大于链表节点个数时，题目意思是旋转链表
        head_num = k % node_num

        first = head
        second = head
        for i in xrange(head_num):
            first = first.next
            # if first.next:
            #     first = first.next
            # else:
            #     # 如果链表中节点数没有k+1个，就不需要做改变
            #     return head
        while first.next:
            first = first.next
            second = second.next
        first.next = head
        head = second.next
        second.next = None
        return head
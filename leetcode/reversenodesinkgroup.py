#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160702

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

思路如下：
以k个节点为一块，将每块内节点连接顺序倒置
当前块的头节点的下一个节点应该改为下一块的头节点
        """
        if k <= 1:
            return head
        ret_head = head
        temp = head
        n = k-1
        while n and temp:
            # print n, temp.val
            temp = temp.next
            n -= 1

        if (not n) and temp:
            # 找到转置后链表的头结点
            ret_head = temp
        else:
            # 如果节点个数没有k个，则直接返回
            return head

        #每一块内链表转置中使用三个指针

        # 指向前一个节点指针
        first = head
        # 指向当前节点指针
        second = head.next
        # 指向下一个节点指针
        third = head.next.next
        while True:
            temp = first
            n = k
            # 判断当前块中个数是否大于等于k
            while n and temp:
                temp = temp.next
                n -= 1
            if n:
                # 当前块节点个数少于k，则返回
                return ret_head

            # 记录下一个块的原始链表中起始位置
            next_part = temp

            # 记录下一个块中转置后起始位置
            next_part_head = None
            n = k - 1
            temp = next_part
            while n and temp:
                temp = temp.next
                n -= 1
            if n or (not temp):
                # 如果下一个块中元素个数小于k，则转置后块的起始位置为原始链表起始位置
                first.next = next_part
            else:
                # 如果下一个块中元素个数不小于k，则转置后块的起始位置为原始链表块的最后一个节点
                first.next = temp
            while third != next_part:
                # 将当前块中节点转置
                second.next = first
                first = second
                second = third
                third = third.next
            second.next = first
            first = next_part
            if first:
                second = first.next
                if second:
                    third = second.next
                else:
                    return ret_head
            else:
                return ret_head

nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 1
head = ListNode(nums[0])
now = head
for i in nums[1:]:
    temp = ListNode(i)
    now.next = temp
    now = now.next
# k = 7
so = Solution()
# head = None
# k = 1
ret = so.reverseKGroup(head, k)
temp = ret
while temp:
    print temp.val
    temp = temp.next
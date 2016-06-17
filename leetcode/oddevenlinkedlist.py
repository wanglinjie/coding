#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160617

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. 
The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

这个题目就是操作链表，可以使用一个指针指向odd链表，另一个指针指向even链表
遍历链表，如果是odd节点则添加到odd链表中，如果是even节点则添加到even节点中
最后将even链表连接到odd链表末尾

注意：确保最后even链表最后一个节点的下一节点为None，否则会导致最后链表中存在一个环

        """
        if (not head) or (not head.next):
            return head
        odd = head
        even_head = head.next
        even = head.next
        num = 1
        now = even.next
        while now:
            if num & 0x1:
                odd.next = now
                odd = odd.next
            else:
                even.next = now
                even = even.next
            # temp = now
            now = now.next
            # temp.next = None
            num += 1
            # num %= 2
        temp = even_head
        # 将even链表最后一个节点next置为None
        while temp and (temp.next != odd):
            temp = temp.next
        if temp:
            temp.next = None

        odd.next = even_head
        return head

nums = [1,2,3,4,5]
head = ListNode(nums[0])
now = head
for i in nums[1:]:
    temp = ListNode(i)
    now.next = temp
    now = now.next

so = Solution()
root = so.oddEvenList(head)
while root:
    print root.val
    root = root.next
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Sort a linked list using insertion sort.
        """
        if (not head) or (not head.next):
            return head
        other = ListNode(0)
        pre = other
        now = head
        while now:
            nextnode = now.next
            pre = other
            while pre.next and pre.next.val <= now.val:
                pre = pre.next
            now.next = pre.next
            pre.next = now
            now = nextnode
        return other.next
'''
ListNode *newHead = new ListNode(INT_MIN);
        while(head) {
            ListNode *cur = head;
            ListNode *p = newHead;
            head = head->next;
            while(p->next && p->next->val<=cur->val) 
                p = p->next;
            cur->next = p->next;
            p->next = cur;
        }
      
        head = newHead->next;
        delete newHead;
        return head;
'''
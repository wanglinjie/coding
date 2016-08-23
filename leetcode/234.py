#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160823


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

对半分，从中间往两边遍历
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # rev, rev.next, slow = slow, rev, slow.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
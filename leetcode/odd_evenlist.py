#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20151222
Last Modified: 
判断两个字符串是否是同字母构成的异序词
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        now = head
        pre_odd = head
        even = head.next
        pre_even = head.next

        num = 1
        while now:
            if num % 2:
                if pre_odd != head:
                    pre_odd.next = now
                    pre_odd = now
            else:
                if pre_even != head.next:
                    pre_even.next = now
                    pre_even = now
            now = now.next
            num += 1
        pre_odd.next = even
        return head

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* now = head;
        ListNode* pre_odd = head;
        ListNode* even = head.next;
        ListNode* pre_even = head.next;
        int num = 1;
        while (now != NULL)
        {
            if (num % 2)
            {
                if (pre_odd != head)
                {
                    pre_odd.next = now;
                    pre_odd = now;
                }
            }
            else
            {
                if (pre_even != head.next)
                {
                    pre_even.next = now;
                    pre_even = now
                }
            }
            now = now.next;
            num += 1;
        pre_odd.next = even;
        return head;
        }

    }
};


class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 1)
            return true;
        float remain;
        remain = n / 3.0;
        while(remain != 1.0)
        {
            if (remain >= 3)
            {
                remain = remain / 3.0;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};

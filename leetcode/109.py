#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160726

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode

Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.
        """
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        ret = self.recursiveBST(node_list)
        return ret
    
    def recursiveBST(self, node_list):
        node_len = len(node_list)
        if not node_len:
            return None
        if node_len == 1:
            return TreeNode(node_list[0].val)
        root_index = (node_len - 1) / 2
        root = TreeNode(node_list[root_index].val)
        left = self.recursiveBST(node_list[:root_index])
        right = self.recursiveBST(node_list[root_index+1:])
        root.left = left
        root.right = right
        return root
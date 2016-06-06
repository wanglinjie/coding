#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160606

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
        """
        if not root:
            return False
        return self.recursive_judge(root, 0, sum)

    def recursive_judge(self, node, now_sum, sum):
        if node and (node.val == (sum-now_sum)) and (not node.left) and (not node.right):
            return True
        return bool((node.left and self.recursive_judge(node.left, now_sum+node.val, sum)) or (node.right and self.recursive_judge(node.right, now_sum+node.val, sum)))


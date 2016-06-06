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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
        """
        if (not root):
            return True
        return self.recursive_judge(root.left, root.right)

    def recursive_judge(self, left, right):
        if (not left) and (not right):
            return True
        if (not left) or (not right) or (left.val != right.val):
            return False
        return self.recursive_judge(left.left, right.right) and self.recursive_judge(left.right, right.left)


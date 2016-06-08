#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160608

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

这道题目就是树的先序遍历，只是最后节点都是父节点的右节点
如果root节点左节点不为空，则新树的root节点的右节点为原先左节点
左子树的最后一个遍历元素需要返回，因为右子树需要连接到该节点
        """
        if not root:
            return

        self.recursive_flatten(root)

        # left = root.left
        # right = root.right

        # if left:
        #     root.right = left
        #     root.left = None
        #     left_last = self.recursive_flatten(left)
        #     left_last.right = right

        # if right:
        #     self.recursive_flatten(right)

        # return root

    def recursive_flatten(self, root):
        if root and (not root.left) and (not root.right):
            return root
        left = root.left
        right = root.right
        left_ret = None
        right_ret = None
        if left:
            root.right = left
            root.left = None
            left_ret = self.recursive_flatten(left)
            left_ret.right = right
        if right:
            right_ret = self.recursive_flatten(right)
        if right_ret:
            return right_ret
        else:
            return left_ret
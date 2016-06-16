#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160616


'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

这道题目就是典型的使用递归来遍历整棵树

这道题目的成功率不高，可能一个原因就是当root为空时，要求返回"[]"，而不是"[""]"
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []

        ret = []
        if root.left:
            left_tree = self.binaryTreePaths(root.left)
            for i in left_tree:
                ret.append(str(root.val)+"->"+i)
        if root.right:
            right_tree = self.binaryTreePaths(root.right)
            for i in right_tree:
                ret.append(str(root.val)+"->"+i)
        if not ret:
            ret.append(str(root.val))
        return ret




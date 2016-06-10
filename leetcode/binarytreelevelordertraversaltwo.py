#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160610

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
        """
        if not root:
            return []
        ret = []
        # 记录当前层需要读取的节点
        read_list = [root]
        # 记录下一层需要读的节点
        next_list = []
        while read_list:
            temp_val = []
            for node in read_list:
                temp_val.append(node.val)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            ret.insert(0, temp_val)
            read_list = next_list
            next_list = []
        return ret
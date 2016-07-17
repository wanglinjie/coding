#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160716

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

Given a binary tree, return the level order traversal of its nodes' values.
 (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

思路：
使用一个队列存储入队节点，在每一层节点之后添加一个None来标志该层节点结束
        """
        if not root:
            return []
        node = root
        nodes = []
        nodes.append(node)
        nodes.append(None)
        ret = []
        temp = []
        while nodes:
            node = nodes[0]
            del nodes[0]
            if (not node):
                if (nodes):
                    nodes.append(None)
                ret.append(temp)
                temp = []
                continue
            temp.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return ret


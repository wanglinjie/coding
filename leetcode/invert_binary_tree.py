#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20151221
Last Modified: 
将二叉树转置
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return 
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
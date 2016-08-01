#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160801

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
Given a binary tree containing digits from 0-9 only, 
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

有根节点到叶子节点构成的整数相加
        """
        result = self.recursiveSum(root)
        ret = 0
        for i in result:
            ret += int(i)
        return ret
    
    def recursiveSum(self, root):
        if not root:
            return []
        ret = []
        str_val = str(root.val)
        if root.left:
            left_result = self.recursiveSum(root.left)
            for i in left_result:
                ret.append(str_val+i)
        if root.right:
            right_result = self.recursiveSum(root.right)
            for i in right_result:
                ret.append(str_val+i)
        if not ret:
            ret.append(str_val)
        return ret
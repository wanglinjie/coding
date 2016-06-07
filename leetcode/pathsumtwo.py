#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160607

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]


Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

这个题目和path sum类似，只是需要保留合适的路径
使用递归
奇怪的是函数明明说返回List[List[int]]类型，但是当不存在合适路径时，返回的是[]
        """
        if (not root) and (not sum):
            return []

        # ret = []
        ret = self.recursivePath(root, sum)
        return ret

    def recursivePath(self, root, sum):
        if root and (not root.left) and (not root.right) and (root.val == sum):
            return [[root.val]]
        ret = []
        if root and root.left:
            temp = [root.val]
            left_ret = self.recursivePath(root.left, sum-root.val)
            if left_ret:
                for i in left_ret:
                    ret.append(temp+i)

        if root and root.right:
            temp = [root.val]
            right_ret = self.recursivePath(root.right, sum-root.val)
            if right_ret:
                for i in right_ret:
                    ret.append(temp+i)
        return ret

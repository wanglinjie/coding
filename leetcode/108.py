#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160726

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nums_len = len(nums)
        if not nums_len:
            return None
        if nums_len == 1:
            return TreeNode(nums[0])
        value_index = (nums_len-1) / 2
        root = TreeNode(nums[value_index])
        left = self.sortedArrayToBST(nums[:value_index])
        right = self.sortedArrayToBST(nums[value_index+1:])
        root.left = left
        root.right = right
        return root

n = 1000
result = []
for i in xrange(n):
    result.append(i)
print result
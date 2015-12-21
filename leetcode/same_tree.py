#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20151221
Last Modified: 
判断两棵树是否完全相同
实验证明leetcode不会判断isinstance(),所以下面代码在leetcode中只能使用注释代码
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if isinstance(p, TreeNode) and isinstance(q, TreeNode):

            if p.val != q.val:
                return False

            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

            return (left and right)
        else:
            return p==q

        # def isSameTree(self, p, q):
        #     if p == None and q == None:
        #         return True
        #     if p and q and p.val == q.val:
        #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        #     return False

p = TreeNode(0)
q = TreeNode(0)
so = Solution()
so.isSameTree(p, q)
print p == q

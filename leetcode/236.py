#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160827

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

Given a binary tree, find the lowest common ancestor (LCA) 
of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes v and w 
as the lowest node in T that has both v and w as descendants 
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. 
Another example is LCA of nodes 5 and 4 is 5, 
since a node can be a descendant of itself according to the LCA definition.

        """
        # if root in (None, p, q): return root
        # left, right = (self.lowestCommonAncestor(kid, p, q)
        #            for kid in (root.left, root.right))
        # return root if left and right else left or right
        if (not root) or (not p) or (not q):
            return None
        p_path = []
        q_path = []
        has_p = self.find_path(root, p, p_path)
        has_q = self.find_path(root, q, q_path)

        if not has_p or not has_q:
            return None

        path_len = min(len(p_path), len(q_path))
        for i in xrange(path_len):
            if p_path[i] != q_path[i]:
                return p_path[i-1]
        return p_path[path_len-1]



    def find_path(self, root, p, p_path):
        if not root:
            return False
        p_path.append(root)
        # 注意：需要判断两个节点是否相同而不是两个节点的值是否相同
        if root == p:
            return True

        result = False
        if root.left:
            result = self.find_path(root.left, p, p_path)
        if (not result) and (root.right):
            result = self.find_path(root.right, p, p_path)
        if not result:
            p_path.pop()
        return result
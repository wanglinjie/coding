#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160725

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
        """
        if n <= 0:
            return 0

        # 当节点个数为1时，binary search trees的数量为1
        record = [1] * (n+1)
        # 没有节点时，数量为0
        record[0] = 0

        # 使用动态规划，记录有n个节点时，binary search trees的数量

        # 总的节点数量
        for i in xrange(2, n+1):
            num = 0
            # 从1到i遍历，以当前位置为根节点
            for j in xrange(1, i+1):
                left = record[j-1]
                right = record[i-j]
                if not left or not right:
                    # 如果左子树或者右子树为空，则数量是左右子树数量相加
                    temp = left + right
                else:
                    # 如果左右子树都不为空，则数量是左右字数数量相乘
                    temp = left * right
                num += temp
            # 记录当前数量节点有的binary search tree数量
            record[i] = num
        print record
        return record[n]

n = 3
so = Solution()
print so.numTrees(n)
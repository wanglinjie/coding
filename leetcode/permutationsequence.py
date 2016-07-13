#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160702
import itertools
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

思路：
将k分解
        """
        permutations = [0] * n
        change_nums = [0] * n
        number = 1
        for i in xrange(n):
            number *= (i+1)
            # 保存第i位之后数字排列个数
            permutations[n - i - 1] = number

        # 因为初始化时就是第一个，所以需要依次求k-1个
        temp = k - 1
        for i in xrange(n):
            if temp >= permutations[i]:
                # 将k分解
                change_nums[i] = temp / permutations[i]
                temp = temp - change_nums[i] * permutations[i]

        ret = []
        for i in xrange(n):
            # 初始化第一个整数
            ret.append(str(i+1))
        for i in xrange(n-1):
            # 获取下一个变换个数
            change_num = change_nums[i+1]
            if change_num:
                # 变换数字
                temp = ret[i+change_num]
                ret[i+1:i+change_num+1] = ret[i:i+change_num]
                ret[i] = temp
                # print ret
        # print ret

        print change_nums
        print permutations
        return "".join(ret)
        
        # plist = itertools.permutations([str(i) for i in range(1, n+1)])
        # for i in range(k-1):
        #     plist.next()
        # return ''.join(plist.next())

# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

n = 9
# k = 24512
k = 12458
so = Solution()
print so.getPermutation(n, k)
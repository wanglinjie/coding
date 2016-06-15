#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160614

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int


Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?


        """
        if not nums:
            return 0

        '''
        下面是使用动态规划，暴力查找，遍历在当前n前面的数字，查看它们的值
        '''
        # nums_len = len(nums)
        # ret = [1] * nums_len
        # for i in xrange(nums_len):
        #     for j in xrange(i-1, -1, -1):
        #         if nums[j] < nums[i]:
        #             ret[i] = max(ret[j]+1, ret[i])
        # return max(ret)


        '''
        下面使用二分查找

下面我们来看一种优化时间复杂度到O(nlgn)的解法，这里用到了二分查找法，所以才能加快运行时间哇。
思路是，我们先建立一个数组ends，把首元素放进去，然后比较之后的元素，
如果遍历到的新元素比ends数组中的首元素小的话，替换首元素为此新元素，
如果遍历到的新元素比ends数组中的末尾元素还大的话，将此新元素添加到ends数组末尾
(注意不覆盖原末尾元素)。
如果遍历到的新元素比ends数组首元素大，比尾元素小时，
此时用二分查找法找到第一个不小于此新元素的位置，覆盖掉位置的原来的数字，
以此类推直至遍历完整个nums数组，此时ends数组的长度就是我们要求的LIS的长度，
特别注意的是ends数组的值可能不是一个真实的LIS，
比如若输入数组nums为{4, 2， 4， 5， 3， 7}，
那么算完后的ends数组为{2， 3， 5， 7}，可以发现它不是一个原数组的LIS，
只是长度相等而已，千万要注意这点。参见代码如下：


在ends数组中，如果当前遍历元素比ends数组中最后一个元素大，则当前元素可以添加到该ends数组中，
因为当前元素和ends列表中元素可以构成一个递增子序列

如果当前元素不比ends最后一个元素大，则可以将当前元素到ends列表中查找第一个比当前元素a大的元素b，
将a替换这个元素。因为如果当前元素之后的递增子序列比ends列表中b之后部分递增子序列长，则将a替换之后
慢慢遍历nums后元素可以将ends中元素替换了
如果当前元素之后的递增子序列比ends列表中b之后部分递增子序列短，则仅仅是替换了元素，对最终结果也没有影响
        '''
        nums_len = len(nums)
        ret = []

        for i in xrange(nums_len):
            left = 0
            right = len(ret)
            while left < right:
                middle = (left + right) / 2
                
                if ret[middle] < nums[i]:
                    left = middle + 1
                else:
                    right = middle
                # print left, right, middle
            if left == len(ret):
                ret.append(nums[i])
            else:
                ret[right] = nums[i]
            # print left, right, ret
        return len(ret)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [6, 2, 5]
so = Solution()
print so.lengthOfLIS(nums)
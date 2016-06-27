#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160627

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float


There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

思路：
如果两个列表中元素个数为奇数个，则返回的元素是中间元素
如果两个列表中元素个数为偶数个，则返回中间两个元素加和的一半
将问题改成寻找两个排序列表中第K个元素

寻找两个列表中第K个元素的思路如下：
使用两个指针，一个指针指向第一个列表，另一个指针指向第二个列表
如果第一个指针指向元素比第二个指针指向元素小，则可以丢弃第一个指针指向的前面元素
如果第二个指针指向元素比第一个指针指向元素小，则可以丢弃第二个指针指向的前面元素
如果两个指针指向元素相等，则指向元素就是第K个元素

递归返回条件：
如果一个列表中元素为空，则就是另一个不为空的第K个元素
如果K为1，则返回的是两个列表中第一个元素中小的那个
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        total_num = len_nums1 + len_nums2
        if total_num & 0x1:
            return self.find_k(nums1, len_nums1, nums2, len_nums2, total_num / 2 + 1)
        else:
            return (self.find_k(nums1, len_nums1, nums2, len_nums2, total_num / 2)
                + self.find_k(nums1, len_nums1, nums2, len_nums2, total_num / 2 + 1))/2.0 

    def find_k(self, nums1, m, nums2, n, k):
        if m > n:
            return self.find_k(nums2, n, nums1, m, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        nums1_index = min(k / 2, m)
        nums2_index = k - nums1_index
        if nums1[nums1_index-1] < nums2[nums2_index-1]:
            return self.find_k(nums1[nums1_index:], m - nums1_index, nums2, n, k - nums1_index)
        elif nums1[nums1_index-1] > nums2[nums2_index-1]:
            return self.find_k(nums1, m, nums2[nums2_index:], n - nums2_index, k - nums2_index)
        else:
            return nums1[nums1_index-1]


nums1 = [1]
nums2 = [1]
so = Solution()
print so.findMedianSortedArrays(nums1, nums2)
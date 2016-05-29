# date:20160529
# -*- coding:utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

核心思想是贪心
倒序遍历列表中节点，查看是否可以到达想要达到的节点

        """
        list_num = len(nums)
        if list_num <= 1:
        	return True

        reach = list_num - 1
        read_num = reach - 1
        while (reach > 0) and (read_num >= 0):
        	if read_num + nums[read_num] >= reach:
        		reach = read_num
        	read_num -= 1
        if reach == 0:
        	return True
        else:
        	return False

A = [3,2,1,0,4]
so = Solution()
if so.canJump(A):
	print "true"
else:
	print "false"

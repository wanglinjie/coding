#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160825

import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

Given an array nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, 
ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?



We scan the array from 0 to n-1, keep "promising" elements in the deque. 
The algorithm is amortized O(n) as each element is put and polled once.

At each i, we keep "promising" elements, 
which are potentially max number in window [i-(k-1),i] or any subsequent window. 
This means

If an element in the deque and it is out of i-(k-1), we discard them. 
We just need to poll from the head, 
as we are using a deque and elements are ordered as the sequence in the array

Now only those elements within [i-(k-1),i] are in the deque. 
We then discard elements smaller than a[i] from the tail. 
This is because if a[x] <a[i] and x<i, 
then a[x] has no chance to be the "max" in [i-(k-1),i], 
or any other subsequent window: a[i] would always be a better candidate.

As a result elements in the deque are ordered in both sequence in array and their value. 
At each step the head of the deque is the max element in [i-(k-1),i]
        """
        if not nums or k <= 0:
            return [0]
        nums_len = len(nums)
        ret = []
        q = collections.deque()
        for i in xrange(nums_len):
            while q and q[0] < i - k + 1:
                q.popleft()
            while q and  nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                ret.append(nums[q[0]])
        return ret


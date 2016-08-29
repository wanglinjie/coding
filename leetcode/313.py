#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160829
import sys

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are 
in the given prime list primes of size k. For example, 
[1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of 
the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
        """
        ret = [1]
        primes_len = len(primes)
        primes_index = [0] * primes_len
        for i in xrange(n-1):
            number = sys.maxint
            j = 0
            for i in xrange(primes_len):
                temp = primes[i] * ret[primes_index[i]]
                while temp == ret[-1]:
                    primes_index[i] += 1
                    temp = primes[i] * ret[primes_index[i]]
                if number > temp:
                    number = temp
                    j = i
            ret.append(number)
            primes_index[j] += 1
        # print ret
        return ret[-1]

        # uglies = [1]
        # merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
        # uniqed = (u for u, _ in itertools.groupby(merged))
        # map(uglies.append, itertools.islice(uniqed, n-1))
        # return uglies[-1]


n = 100
primes = [2, 3, 5, 7]
so = Solution()
print so.nthSuperUglyNumber(n, primes)
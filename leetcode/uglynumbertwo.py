# date:20160527

import heapq
# import itertools
# class Solution(object):
#     def nthSuperUglyNumber(self, n, primes):
#         """
#         :type n: int
#         :type primes: List[int]
#         :rtype: int


# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note that 1 is typically treated as an ugly number.
#         """
#         uglies = [1]
#         merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
#         uniqed = (u for u, _ in itertools.groupby(merged))
#         map(uglies.append, itertools.islice(uniqed, n-1))
#         return uglies[-1]

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return []
        uglys = [1]
        i = j = k = 0
        for num in xrange(n - 1):
            uglys.append(min(uglys[i] * 2, uglys[j] * 3, uglys[k] * 5))
            if uglys[-1] == uglys[i] * 2:
                i += 1
            if uglys[-1] == uglys[j] * 3:
                j += 1
            if uglys[-1] == uglys[k] * 5:
                k += 1
        return uglys[-1]

so = Solution()
print so.nthUglyNumber(1311)




# so = Solution()
# print so.nthSuperUglyNumber(4, [2, 5, 7, 13])


# class Solution {
# public:
#     int nthUglyNumber(int n) {
#         vector <int> results(1, 1);
#         int i = 0, j = 0, k = 0;
#         while (results.size() < n)
#         {
#             results.push_back(min(results[i] * 2, min(results[j] * 3, results[k] * 5)));
#             if (results.back() == results[i] * 2) ++i;
#             if (results.back() == results[j] * 3) ++j;
#             if (results.back() == results[k] * 5) ++k;
#         }
#         return results.back();
#     }
# };

# import heapq  
# import random  
  
# heap = []  
# heapq.heapify(heap)  
# for i in range(15):  
#   item = random.randint(10, 100)  
#   print "comeing ", item,  
#   if len(heap) >= 5:  
#     top_item = heap[0] # smallest in heap  
#     if top_item < item: # min heap  
#       top_item = heapq.heappop(heap)  
#       print "pop", top_item,  
#       heapq.heappush(heap, item)  
#       print "push", item,  
#   else:  
#     heapq.heappush(heap, item)  
#     print "push", item,  
#   pass  
#   print heap  
# pass  
# print heap  
  
# print "sort"  
# heap.sort()  
  
# print heap 
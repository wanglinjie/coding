# import heapq
# import itertools
# class Solution(object):
#     def nthSuperUglyNumber(self, n, primes):
#         """
#         :type n: int
#         :type primes: List[int]
#         :rtype: int
#         """
#         uglies = [1]
#         merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
#         uniqed = (u for u, _ in itertools.groupby(merged))
#         map(uglies.append, itertools.islice(uniqed, n-1))
#         return uglies[-1]


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
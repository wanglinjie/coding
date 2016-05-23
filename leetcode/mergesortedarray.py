# date:20160521
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space 
(size that is greater or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
        """
        if not m:
            # 注意python中传入列表，类似于c语言中指针，如果改变指针变量指向，原始指针并不会改变
            # 如果改变指针列表中的值，则调用函数中列表页会受变化
            # 这题中下面代码是改变列表中值
            # 如果改成num1 = nums2，则这仅仅改变了num1这个形参的指向列表，而并没有改变调用函数中列表值
            nums1[:] = nums2[:]
            # nums1.extend(nums2[:])
            return
        if len(nums1) > m:
            del nums1[m:]
            # nums1 = nums2
        point1 = 0
        point2 = 0
        while (point1 < m) and (point2 < n):
            if nums1[point1] < nums2[point2]:
                point1 += 1
            else:
                nums1.insert(point1, nums2[point2])
                m += 1
                point1 += 1
                point2 += 1
        # 注意当nums1中元素遍历完但是nums2中元素没有遍历完时，应该讲nums2中元素添加在nums1后
        if point2 < n:
            nums1.extend(nums2[point2:])
# nums1 = [2, 7]
# m = 2
# nums2 = [1, 3, 4, 6, 7, 9]
# n = 6
nums1 = [0]
m = 0
nums2 = [1]
n = 1
so = Solution()
so.merge(nums1, m, nums2, n)
print nums1
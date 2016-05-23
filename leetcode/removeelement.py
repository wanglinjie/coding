class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_length = len(nums)
        for i in xrange(nums_length-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


so = Solution()
nums = [3, 2, 2, 3]
val = 3
print so.removeElement(nums, val)
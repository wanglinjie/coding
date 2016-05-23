class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_nums = sorted(nums)
        i = 0
        j = len(new_nums) - 1
        while i < j:
            if new_nums[i] + new_nums[j] == target:
                return sorted([nums.index(new_nums[i]), nums.index(new_nums[j])])
            elif new_nums[i] + new_nums[j] < target:
                i += 1
            elif new_nums[i] + new_nums[j] > target:
                j -= 1


so = Solution()
print so.twoSum([1, 2, 3], 4)
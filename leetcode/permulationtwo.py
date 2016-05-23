# date:20160520
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
        """
        if len(nums) <= 1:
            return [nums]
        results = []
        read = []
        for i, j in enumerate(nums):
            # print j
            if j in read:
                continue
            read.append(j)
            new_nums = copy.deepcopy(nums)
            del new_nums[i]
            tempresults = self.permute(new_nums)
            for tempresult in tempresults:
                tempresult.append(j)
                results.append(tempresult)
                # print results[-1]
        # print results
        return results

so = Solution()
print so.permute([1, 1, 2, 4, 1])
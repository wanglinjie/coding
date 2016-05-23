# date:20160520
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
        """
        if len(nums) <= 1:
            return [nums]
        results = []
        for i, j in enumerate(nums):
            # print j
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
print so.permute([1, 2, 3, 4, 5, 6])
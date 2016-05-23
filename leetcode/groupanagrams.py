#date:20160521
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
        """
        results = []
        group = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in group:
                group[temp] = []
            group[temp].append(i)

        for i in group:
            results.append(sorted(group[i]))
        return results


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
so = Solution()
print so.groupAnagrams(strs)
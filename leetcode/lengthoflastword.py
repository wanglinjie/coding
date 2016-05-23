# date:20160509
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_split = s.split(" ")
        if s_split:
            return len(s_split[-1])
        else:
            return 0



s = "a "
so = Solution()
print so.lengthOfLastWord(s)
# date:20160514

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        :Reverse String
        """
        if not s:
            return ""
        s = list(s)
        s.reverse()
        return "".join(s)

so = Solution()
print so.reverseString("hello")
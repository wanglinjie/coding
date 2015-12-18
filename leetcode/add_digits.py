class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num:
            print 1 + (num - 1) % 9
        else:
            print 0
        # print (1+((num -1) % 9)) if num  else 0


so = Solution()
so.addDigits(0)
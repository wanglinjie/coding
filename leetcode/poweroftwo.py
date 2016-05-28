# date:20160527
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
Given an integer, write a function to determine if it is a power of two.
        """
        if n <= 0:
            return False
        # while not (n & 0x1):
        #     n = n >> 1
        # if n == 1:
        #     return True
        # else:
        #     return False

        # if (n & (n -1)):
        #     return False
        # else:
        #     return True
        return (0 == (n & (n - 1)))

so = Solution()
if so.isPowerOfTwo(32):
    print "True"
else:
    print "False"

print bin(12).count('1')
# date:20160522

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

Implement int sqrt(int x).

Compute and return the square root of x.
        """
        if x == 1:
            return x
        low = 0
        high = x
        result = self.findSqrt(low, high, x)
        return result

    def findSqrt(self, low, high, x):
        if (low + 1) >= high:
            return low
        middle = low + (high - low) / 2
        if (middle ** 2) < x:
            return self.findSqrt(middle, high, x)
        elif (middle ** 2) > x:
            return self.findSqrt(low, middle, x)
        else:
            return middle

so = Solution()
print so.mySqrt(5)
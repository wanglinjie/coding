# date:20160509
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        result = 1
        m = n
        if n < 0:
            m = -n
        # for i in xrange(m):
        #     result *= x
        # if n < 0:
        #     if not result:
        #         return 0
        #     result = 1 / result
        # return result
        if m & 0x1:
            half_result = self.recurPow(x, m>>1)
            result = half_result * half_result * x
        else:
            half_result = self.recurPow(x, m>>1)
            result = half_result * half_result
        if n < 0:
            if not result:
                return 0
            result = 1 / result
        return result



    def recurPow(self, x, n):
        if n == 0:
            return 1.0
        result = 1
        if n & 0x1:
            half_result = self.recurPow(x, n>>1)
            result = half_result * half_result * x
        else:
            half_result = self.recurPow(x, n>>1)
            result = half_result * half_result
        return result


x = 2
n = 8
so = Solution()
print so.myPow(x, n)
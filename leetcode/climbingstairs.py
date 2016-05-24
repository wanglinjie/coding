# -*- coding:utf-8 -*-
# date:20160523

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

当n大于3事，到n的前一步有经过一步到n还有直接走两步到n，所以总的到n的选择有f(n-1)+f(n-2)种
        """
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        first = 1
        second = 2
        result = 0
        for i in xrange(3, n+1):
            result = first + second
            first = second
            second = result
        return result

so = Solution()
print so.climbStairs(5)
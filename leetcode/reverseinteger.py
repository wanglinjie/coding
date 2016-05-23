# date:20160514

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        :Reverse digits of an integer.
        """
        if x >= 0:
            temp = x
        else:
            temp = -x
        temp = list(str(temp))
        temp.reverse()
        result = int("".join(temp))
        if x < 0:
            # 注意判断
            if result > 2147483648:
                result = 0
            else:
                result = -result
        elif result > 2147483647:
            result = 0

        return result


so = Solution()
print so.reverse(1534236469)
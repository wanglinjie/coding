# date:20160526
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
        """
        if num <= 1:
            if num <= 0:
                return False
            return True
        while not (num & 0x1):
            num = num >> 1
        run = True
        while run:
            run = False
            if not (num % 3):
                num /= 3
                run = True
            if not (num % 5):
                num /= 5
                run = True
        if num == 1:
            return True
        else:
            return False

so = Solution()
if so.isUgly(-2147483648):
    print "True"
else:
    print "False"
# date:20160522
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
        """
        one = 1
        new_digits = []
        for i in xrange(len(digits)-1, -1, -1):
            num = digits[i] + one
            one = num / 10
            num = num % 10
            new_digits.insert(0, num)

        if one:
            new_digits.insert(0, one)
        return new_digits


digits = [1, 2, 3, 4]
so = Solution()
print so.plusOne(digits)


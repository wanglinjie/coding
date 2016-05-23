# date:20160514

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        :Palindrome Number Determine whether an integer is a palindrome. Do this without extra space.
        """
        # if x < 0:
        #     return False
        # is_palindrome = True
        # x_list = list(str(x))
        # head = 0
        # last = len(x_list) - 1
        # while head < last:
        #     if x_list[head] != x_list[last]:
        #         is_palindrome = False
        #         return is_palindrome
        #     head += 1
        #     last -= 1
        # return is_palindrome
        if x < 0:
            return False
        else:
            y = 0
            temp = x
            while temp != 0:
                y = y * 10 + temp % 10
                temp = temp / 10
            if y == x:
                return True
            else:
                return False

so = Solution()
print so.isPalindrome(0)

#-2147483648

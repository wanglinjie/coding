# date:20160526

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
        """
        low = 1
        high = n
        result = self.recursiveFind(low, high)
        return result

    def recursiveFind(self, low, high):
        if (low + 1) >= high:
            if isBadVersion(low):
                return low
            else:
                return high
        middle = low + (high - low) / 2
        if isBadVersion(middle):
            return self.recursiveFind(low, middle)
        else:
            return self.recursiveFind(middle, high)

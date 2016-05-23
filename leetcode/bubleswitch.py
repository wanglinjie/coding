import math
class Solution(object):
    def factorNum(self, m):
        num = 0
        # for i in xrange(m):
        #     if (m) % (i+1) == 0:
        #         num += 1
        # return num
        # for i in xrange(int(math.sqrt(m))):
        #     if m % (i+1):
        #         num += 1
        # num *= 2
        # if m % (int(math.sqrt(m))):
        #     return num
        # else:
        #     return num -1
        if math.sqrt(m) > int(math.sqrt(m)):
            return 0
        else:
            return 1

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        lighton = []
        # for i in xrange(n):
        #     num = self.factorNum(i+1)
        #     if num % 2:
        #         lighton.append(i+1)
        # return len(lighton)
        for i in xrange(n):
            if self.factorNum(i+1):
                lighton.append(i+1)
        print lighton
        return len(lighton)


so = Solution()
print so.bulbSwitch(9)
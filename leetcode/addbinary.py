# date:20160528
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
        """
        if not a:
            return b
        if not b:
            return a
        result = []
        a_list = list(a)
        a_list.reverse()
        b_list = list(b)
        b_list.reverse()
        a_num = len(a_list)
        b_num = len(b_list)
        i = 0
        j = 0
        while (i < a_num) and (i < b_num):
            total = int(a_list[i]) + int(b_list[i]) + j
            result.append(str(total % 2))
            j = total / 2
            i += 1

        while i < a_num:
            total = int(a_list[i]) + j
            result.append(str(total % 2))
            j = total / 2
            i += 1

        while i < b_num:
            total = int(b_list[i]) + j
            result.append(str(total % 2))
            j = total / 2
            i += 1
        if j != 0:
            result.append(str(j))
        result.reverse()
        return "".join(result)



so = Solution()
print so.addBinary("1", "111")
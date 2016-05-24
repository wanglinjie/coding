# date:20160524
from itertools import izip
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains 
lowercase letters separated by a single space.
        """
        pattern_dict = {}
        pattern_num = []

        str_dict = {}
        str_num = []

        for i in pattern:
            if i not in pattern_dict:
                pattern_dict[i] = 0
            pattern_dict[i] += 1
        for i in pattern_dict:
            pattern_num.append(pattern_dict[i])
        pattern_num = sorted(pattern_num)

        str_list = str.split()
        for i in str_list:
            if i not in str_dict:
                str_dict[i] = 0
            str_dict[i] += 1
        for i in str_dict:
            str_num.append(str_dict[i])
        str_num = sorted(str_num)

        if len(pattern_num) != len(str_num):
            return False
        # for i, j in izip(pattern_num, str_num):
        #     if i != j:
        #         return False
        for i in xrange(len(pattern_num)):
            if pattern_num[i] != str_num[i]:
                return False
        return True


pattern = "ab"
string = "dog  a"
so = Solution()
if so.wordPattern(pattern, string):
    print "true"
else:
    print "false"


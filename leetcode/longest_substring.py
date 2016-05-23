
# date:20160509
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_length = 0
        s_list = list(s)
        temp_list = []
        for i in s_list:
            if i in temp_list:
                if len(temp_list) > longest_length:
                    longest_length = len(temp_list)
                i_index = temp_list.index(i)
                del temp_list[0:i_index + 1]
            temp_list.append(i)
        if len(temp_list) > longest_length:
            longest_length = len(temp_list)
        return longest_length







        # s_list = list(s)
        # longest_length = 0
        # temp_string = ""

        # for i in s:
        #     if i not in temp_string:
        #         temp_string += i
        #     else:
        #         if len(temp_string) > longest_length:
        #             longest_length = len(temp_string)
        #         temp_string = i
        # if len(temp_string) > longest_length:
        #     longest_length = len(temp_string)
        # return longest_length


s = "asdfskdajsfkaas"
so = Solution()
print so.lengthOfLongestSubstring(s)
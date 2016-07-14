#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160713

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]

Given an array of words and a length L, 
format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; 
that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, 
it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
        """
        results = []
        temp = []
        temp_len = 0
        for i in words:
            i_len = len(i)
            new_len = 0
            if temp_len:
                new_len = temp_len + i_len + 1
            else:
                new_len = i_len
            if new_len <= maxWidth:
                temp.append(i)
                temp_len = new_len
            else:
                self.addSpace(temp, maxWidth, False)
                results.append("".join(temp))
                # results.append(temp)
                temp = []
                temp.append(i)
                temp_len = len(i)

        self.addSpace(temp, maxWidth, True)
        results.append("".join(temp))
        # results.append(temp)
        return results

    def addSpace(self, result, maxWidth, isLast):
        result_num = len(result) - 1
        result_len = 0
        for i in result:
            result_len += len(i)
        space_len = maxWidth - result_len
        if not result_num:
            result.append(" " * space_len)
        else:
            if isLast:
                for j in xrange(result_num):
                    result.insert(2 * j + 1, " ")
                result.append(" " * (space_len - result_num))
            else:
                mean_space = space_len / result_num
                remain_space = space_len % result_num
                for j in xrange(result_num):
                    if remain_space:
                        add_space = " " * (mean_space+1)
                        remain_space -= 1
                    else:
                        add_space = " " * mean_space
                    result.insert(2 * j + 1, add_space)



# words = ["This", "is", "an", "example", "of", "text", "justification."]
# L = 16
# words = [""]
# L = 0
words = ["What","must","be","shall","be."]
L = 12
so = Solution()
print so.fullJustify(words, L)



# ["What must be","shall    be."]
# ["What must be","shall be.   "]
# ['What must be', 'shall be.   ']

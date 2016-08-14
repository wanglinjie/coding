#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160814

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]

思路：
顺序遍历获取连续10个字符组成的字符串
使用hash记录该字符串是否之前已经存在了
如果存在则保存该字符串
        """
        # return [k for k,v in collections.Counter(s[i:i+10] for i in range(len(s)-9)).iteritems() if v>1]
        repeatSeq = set()
        addedSeq = set()
        result = []
        answer = []
        charToBin = {'A' : 0b00, 'T' : 0b01, 'G' : 0b10, 'C' : 0b11}
        mask = 0xfffff
        current = 0
        for i in range(len(s)):
            #create bit
            x = charToBin[s[i]]
            current |= x
            if i >= 9:
                if current in repeatSeq:
                    if current not in addedSeq:
                        addedSeq.add(current)
                        result.append(i - 9)
                else:
                    repeatSeq.add(current)
            #shift
            current <<= 2
            #mask
            current &= mask
        for i in result:
            answer.append(s[i : i + 10])
        return answer
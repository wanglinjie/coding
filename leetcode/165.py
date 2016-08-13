#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160813

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . 
character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
        """
        version_1_split = version1.split(".")
        version_1_split = [int(i) for i in version_1_split]
        version_1_len = len(version_1_split)
        version_2_split = version2.split(".")
        version_2_split = [int(i) for i in version_2_split]
        version_2_len = len(version_2_split)
        min_len = min(version_1_len, version_2_len)
        for i in xrange(min_len):
            # 判断version1和version2中各个.分割的数字大小
            if version_1_split[i] < version_2_split[i]:
                return -1
            elif version_1_split[i] > version_2_split[i]:
                return 1
  
                
        if version_1_len < version_2_len:
            # 如果version2比version1中数字多
            for i in xrange(min_len, version_2_len):
                # 只要不为0，则证明version2版本比version1高
                if version_2_split[i] != 0:
                    return -1
        elif version_1_len > version_2_len:
            for i in xrange(min_len, version_1_len):
                if version_1_split[i] != 0:
                    return 1
        return 0
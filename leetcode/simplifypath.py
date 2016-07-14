#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160713

import sys
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
        """
        
        # path_len = len(path)
        # for i in xrange(path_len):
        #     if path[i] == "/":
        #         continue
        #     if path[i] == ".":
        #         if path[i+1] == ".":
        #             del sim_path[-1]
        #         elif path[i+1] == "/":
        #             continue
        #     else:
        #         sim_path.append(path[i])
        sim_path = []
        # 使用“/”切分路径
        path_split = path.split("/")
        for i in path_split:
            # 遇到单独“.”或者遇到空格，则不做任何处理
            if (i == ".") or (not i):
                continue
            # 遇到“..”则需要往回退一层路径，即需要将路径中元素弹出一个
            if i == "..":
                if sim_path:
                    del sim_path[-1]
            else:
                # 遇到文件夹名，则需要入栈
                sim_path.append(i)
        ret = "/".join(sim_path)
        return "/" + ret

        


path = "/../.."
so = Solution()
print so.simplifyPath(path)
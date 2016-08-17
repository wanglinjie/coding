#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date；20160817

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3


思路：
遍历元素，如果当前元素是“1”,则从当前位置先深搜索
每个遍历的元素是“1”的添加到read中
每次先深搜索都可以将一块陆地遍历
所以有几次先深搜索，则有几块陆地
        """
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        ret = 0
        read = set()
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "1":
                    if (i, j) in read:
                        continue
                    queue = []
                    queue.append((i,j))
                    while queue:
                        point = queue[-1]
                        del queue[-1]
                        x, y = point[0], point[1]
                        read.add((x,y))
                        # print x, y
                        if x > 0 and grid[x-1][y] == "1":
                            if (x-1,y) not in read:
                                queue.append((x-1,y))
                        if y > 0 and grid[x][y-1] == "1":
                            if (x, y-1) not in read:
                                queue.append((x, y-1))
                        if x < (m-1) and grid[x+1][y] == "1":
                            if (x+1, y) not in read:
                                queue.append((x+1, y))
                        if y < (n-1) and grid[x][y+1] == "1":
                            if (x, y+1) not in read:
                                queue.append((x, y+1))
                    ret += 1
        return ret

# grid = ["11110","11010","11000","00001"]
grid = ["1","1"]
so = Solution()
print so.numIslands(grid)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160825

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            row,col,width=len(matrix)-1,0,len(matrix[0])
            while row>=0 and col<width:
                if matrix[row][col]==target:
                    return True
                elif matrix[row][col]>target:
                    row -= 1
                else:
                    col += 1
            return False


# 另外一个方法，思路很巧妙
 # public bool SearchMatrix(int[,] matrix, int target)
 #    {
 #        return SearchMatrix(matrix, target, 0, matrix.GetLength(1)-1, 0, matrix.GetLength(0)-1);
 #    }
    
 #    public bool SearchMatrix(int[,] matrix, int target, int left, int right, int top, int bottom)
 #    {
 #        if (left>right || top>bottom)
 #            return false;
        
 #        int lt = left;
 #        int r = right;
 #        int t = top;
 #        int b = bottom;
        
 #        while (lt<=r && t<=b)
 #        {
 #            int midx = (lt + r)/2;
 #            int midy = (t + b)/2;
 #            int val = matrix[midy, midx];
 #            if (target < val)
 #            {
 #                r = midx-1;
 #                b = midy-1;
 #            }
 #            else if (target > val)
 #            {
 #                lt = midx+1;
 #                t = midy+1;
 #            }
 #            else 
 #                return true;
 #        }
        
 #        return SearchMatrix(matrix, target, lt,right,top,b)
 #            || SearchMatrix(matrix, target, left,r,t,bottom);
 #    }
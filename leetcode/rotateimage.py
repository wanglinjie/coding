# date:20160520

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
        """
        i = 0
        j = len(matrix) - 1
        while i < j:
            k = i
            d = j
            while k < j:
                t = matrix[i][k]
                matrix[i][k] = matrix[d][i]
                matrix[d][i] = matrix[j][d]
                matrix[j][d] = matrix[k][j]
                matrix[k][j] = t
                k += 1
                d -= 1
            i += 1
            j -= 1
  

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
so = Solution()
so.rotate(matrix)
print matrix
# problem.73: Given a matrix, if an element is 0, set its entire row and column to 0. Modify the matrix in-place.

# Approach:
# Create two arrays to track which rows and columns contain 0.
# Traverse the matrix and mark the corresponding row/column when matrix[i][j] == 0.
# Traverse again and set matrix[i][j] = 0 if its row or column was marked.

# Time Complexity: O(m × n)
# Space Complexity: O(m + n)


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0 for _ in range(r)]
        cols_track = [0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if(matrix[i][j] == 0):
                    row_track[i] = -1
                    cols_track[j] = -1

        for i in range(r):
            for j in range(c):
                if(row_track[i] == -1 or cols_track[j] == -1):
                    matrix[i][j] = 0

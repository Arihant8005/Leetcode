# problem.48: Rotate an n × n matrix 90° clockwise in-place without using another matrix.

# Approach:
# Your solution uses 2 steps:

# Transpose the matrix
# Swap matrix[i][j] with matrix[j][i].
# This converts rows into columns.
# Reverse every row
# matrix[i].reverse() reverses each row.
# Together, transpose + reverse gives a 90° clockwise rotation.

# Time Complexity: O(n²)
# Space Complexity: O(1) — the matrix is modified in-place.

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
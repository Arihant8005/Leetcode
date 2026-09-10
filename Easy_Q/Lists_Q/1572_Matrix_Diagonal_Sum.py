# problem.1572: Find the sum of the two diagonals of a square matrix. If the matrix has an odd size, don't count the center element twice.

# Approach:
# mat[i][i] → primary diagonal.
# mat[i][n-1-i] → secondary diagonal.
# If both positions are the same (center element), add it only once using:
# if i != n - 1 - i.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]
            if(i != n-1-i):
                total += mat[i][n-1-i]
        
        return total
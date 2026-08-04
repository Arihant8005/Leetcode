# problem.1351: Given a m x n matrix grid which is sorted in non-increasing order 
# both row-wise and column-wise, return the number of negative numbers in grid.

# Approach:
# Traverse every element in the matrix and increment the count whenever a negative number is found.

# Time Complexity: O(m × n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neg = 0
        for i  in range(rows):
            for j in range(cols):
                if(grid[i][j] < 0):
                    neg += 1

        return neg
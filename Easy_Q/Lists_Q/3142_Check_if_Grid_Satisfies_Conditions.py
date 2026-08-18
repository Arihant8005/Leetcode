# problem.3142: Given a binary matrix grid, return True if it satisfies these conditions:
# Every cell must be equal to the cell directly below it.
# Every cell must be different from the cell directly to its right.
# Otherwise, return False.

# Approach:
# Traverse every cell and ensure the value below is equal while the value to the right is different.

# Time complexity: O(m × n)
# Space complexity: O(1)

from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:


        for i in range(len(grid)):
            for j in range(len(grid[0])):


                if i + 1 < len(grid) and grid[i][j] != grid[i + 1][j]:
                    return False


                if j + 1 < len(grid[0]) and grid[i][j] == grid[i][j + 1]:
                    return False


        return True
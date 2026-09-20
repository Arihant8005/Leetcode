# problem.3898: Given a matrix, find the sum of each row and return the sums as a list.

# Approach:
# Traverse each row of the matrix.
# Use sum() to calculate the sum of each row.
# Append each sum to ans.
# Return ans.

# Time Complexity: O(m × n) — where m is the number of rows and n is the number of elements per row.
# Space Complexity: O(m) — for the result list.

from typing import List

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        
        for val in matrix:
            ans.append(sum(val))
        
        return ans
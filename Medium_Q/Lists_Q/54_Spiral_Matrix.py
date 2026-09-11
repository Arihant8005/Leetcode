# problem.54: Return the elements of a matrix in spiral order, starting from the top-left and moving clockwise toward the center.

# Approach:
# top → top row
# bottom → bottom row
# left → left column
# right → right column

# In each iteration:

# Traverse the top row from left → right.
# Traverse the right column from top → bottom.
# Traverse the bottom row from right → left.
# Traverse the left column from bottom → top.
# Move the boundaries inward.
# The if conditions prevent adding elements twice when the remaining portion has only one row or column.

# Time Complexity: O(m × n), where m is the number of rows and n is the number of columns.
# Space Complexity: O(m × n) — for the result list.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []

        while(top <= bottom and left <= right):
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if(top <= bottom):
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if(left <= right):
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result
                
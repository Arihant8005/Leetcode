# problem.1886: Given two binary matrices mat and target, check whether mat can be rotated by 0°, 90°, 180°, or 270° to become equal to target.

# Approach:
# Check if mat is equal to target.
# If not, rotate mat by 90° clockwise using transpose and row reversal.
# Repeat this process up to 4 times.
# Return True if both matrices become equal; otherwise, return False.

# Time Complexity: O(n²)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if(mat == target):
                return True

            for i in range(n - 1):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
            for i in range(n):
                mat[i].reverse()
        
        return False
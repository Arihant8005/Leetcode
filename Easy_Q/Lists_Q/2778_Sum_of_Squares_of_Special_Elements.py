# problem.2778: Given an array nums, find the sum of squares of all elements whose 1-based index divides n (where n = len(nums)).

# Approach:
# Iterate through every index i.
# Since the problem uses 1-based indexing, check n % (i + 1) == 0.
# If true, add nums[i]² to total.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            if(n % (i+1) == 0):
                total = total + nums[i] * nums[i]
        return total
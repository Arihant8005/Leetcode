# problem.268: Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array

# Approach:
# Calculate the expected sum from 0 to n, subtract the actual sum of nums, and return the difference.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        natural_sum = (n * (n + 1)) // 2

        return natural_sum - sum(nums)
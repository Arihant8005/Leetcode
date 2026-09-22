# problem.3978: Given an array nums, determine whether the middle element appears exactly once in the array.

# Approach:
# Find the middle element using nums[len(nums) // 2].
# Use count() to count how many times it appears.
# Return True if its count is exactly 1, otherwise return False.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:

        return nums.count(nums[len(nums) // 2]) == 1
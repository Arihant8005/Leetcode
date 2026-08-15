# problem.3925: Given an integer array nums, create a new array by concatenating nums with its reverse. Return the resulting array.

# Approach:
# Copy the original array into the first half and copy its elements from right to left into the second half.

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = nums[i]

        for i in range(n):
            ans[i + n] = nums[n - i - 1]

        return ans
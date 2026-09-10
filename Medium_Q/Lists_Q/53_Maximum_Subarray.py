# problem.53: Find the maximum sum of a contiguous subarray in nums.

# Approach:
# Your solution uses Kadane's Algorithm:
# Keep adding elements to total.
# Update max_sum with the largest sum found so far.
# If total becomes negative, reset it to 0 because a negative sum cannot help the next subarray.
# Return max_sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        max_sum = float("-inf")
        for i in range(n):
            total += nums[i]
            max_sum = max(total, max_sum)
            if(total < 0):
                total = 0
        return max_sum


# problem.1991: Given an integer array nums, find the middle index where the sum of elements to the left equals the sum of elements to the right. Return -1 if no such index exists.

# Approach:
# Calculate the total sum of the array.
# Maintain a running left_sum.
# For each index:
# right_sum = total - left_sum - nums[i]
# If left_sum == right_sum, return the index.
# Add nums[i] to left_sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
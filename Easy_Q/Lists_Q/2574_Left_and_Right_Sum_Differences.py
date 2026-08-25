# problem.2574: Given an array nums, return an array where each element is the absolute difference between the sum 
# of elements to its left and the sum of elements to its right.

# Approach
# Calculate the total sum of the array.
# Maintain left sum.
# For each element, calculate right = total - left - nums[i].
# Add abs(left - right) to the result.
# Update left.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        total = sum(nums)
        left = 0
        n = len(nums)
        for i in range(n):
            right = total - left - nums[i]
            result.append(abs(left - right))
            left += nums[i]
        return result

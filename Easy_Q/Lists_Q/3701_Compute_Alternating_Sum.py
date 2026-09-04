# problem.3701: Given an array nums, calculate the alternating sum by adding elements at even indices and subtracting elements at odd indices.

# Approach:
# Traverse the array.
# Add elements at even indices to even_sum.
# Add elements at odd indices to odd_sum.
# Return even_sum - odd_sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_sum = 0
        odd_sum = 0
        for i in range(len(nums)):
            if(i % 2 == 0):
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
        return even_sum - odd_sum
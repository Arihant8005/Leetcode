# problem.2176: Given an integer array nums and an integer k, count pairs (i, j) where:
# i < j
# nums[i] == nums[j]
# (i * j) % k == 0

# Approach:
# Use two nested loops to check every possible pair.
# For each pair, check whether the values are equal and i * j is divisible by k.
# If both conditions are true, increment count.

# Time Complexity: O(n²)
# Space Complexity: O(1)

from typing import List

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:

        count = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if(nums[i] == nums[j] and (i*j) % k == 0):
                    count += 1

        return count


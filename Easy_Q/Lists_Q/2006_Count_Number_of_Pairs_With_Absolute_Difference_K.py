# problem.2006: Given an integer array nums and an integer k, count the number of pairs (i, j) such that:
# i < j and |nums[i] - nums[j]| = k.

# Approach:
# Store the frequency of every number in a dictionary.
# For each val, check if val + k exists.
# Add its frequency to count.
# This counts all valid pairs without using nested loops.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        dist = {}
        for val in nums:
            dist[val] = dist.get(val, 0) + 1
        for val in nums:
            if val+k in dist:
                count += dist[val+k]
        return count

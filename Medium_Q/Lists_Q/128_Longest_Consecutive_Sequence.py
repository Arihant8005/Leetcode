# problem.128: Given an integer array nums, find the length of the longest consecutive sequence of integers.

# Approach:
# Convert nums into a set for O(1) average lookup.
# For each number, start a sequence only if val - 1 is not present.
# Keep checking val + 1 to find the sequence length.
# Update the maximum length.

# Time Complexity; O(n) — each number is processed a constant number of times on average.
# Space Complexity: O(n) — for the set.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        my_set = set(nums)
        for val in my_set:
            if val-1 not in my_set:
                count = 1
                temp = val
                while temp+1 in my_set:
                    count += 1
                    temp += 1
                max_count = max(count, max_count)
        
        return max_count
            
# problem.3718: Given an array nums and an integer k, find the smallest positive multiple of k that is not present in nums.

# Approach:
# Store all elements of nums in a set for fast lookup.
# Start checking multiples of k from k.
# Return the first multiple that is not in the set.

# Time Complexity: O(n + m) — where m is the number of multiples checked.
# Space Complexity: O(n)

from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set1 = set(nums)
        i = 1
        while(True):
            if k * i not in set1:
                return k * i
            i += 1
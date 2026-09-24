# problem.4049: Given an array nums, count the distinct values whose occurrence positions form an arithmetic progression and the value appears at least 3 times.

# Approach:
# Store all indices of each value using a dictionary.
# For each value appearing at least 3 times, calculate the gap between its first two positions.
# Check whether all consecutive positions have the same gap.
# If yes, count that value.

# Time Complexity: O(n) — all indices are processed once overall.
# Space Complexity: O(n) — for the dictionary storing positions.

from typing import List
from collections import defaultdict

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        count = 0
        for val in pos.values():
            if(len(val) < 3):
                continue
            gap = val[1] - val[0]
            special = True
            for i in range(2, len(val)):
                if(val[i] - val[i-1] != gap):
                    special = False
                    break
            if(special):
                count += 1

        return count
            
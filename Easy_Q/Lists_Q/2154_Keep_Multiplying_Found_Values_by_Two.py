# problem.2154: Given an array nums and an integer original, repeatedly multiply original by 2 as long as it exists in nums. Return the final value.

# Approach:
# While original is present in nums, multiply it by 2.
# Stop when original is not present.
# Return original.

# Time Complexity: O(n × k) — in search takes O(n), repeated k times.
# Space Complexity: O(1)

from typing import List

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while(original in nums):
            original *= 2
        
        return original
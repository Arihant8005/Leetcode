# problem.2206: Given an array nums, check whether the elements can be divided into pairs such that each pair contains equal elements.

# Approach:
# Count the frequency of each element using Counter.
# If any element appears an odd number of times, return False.
# Otherwise, return True.

# Time Complexity: O(n)
# Space Complexity: O(n)


from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for val in freq.values():
            if(val % 2 != 0):
                return False
        return True
            
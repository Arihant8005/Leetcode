# problem.1748: Given an array nums, return the sum of all elements that appear exactly once.

# Approach
# Count the frequency of each element using Counter.
# Traverse the frequency map.
# Add elements whose frequency is 1.

# Time Complexity: O(n)

# Space Complexity: O(n)

from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        unique = Counter(nums)
        for key, val in unique.items():
            if(val == 1):
                sum += key
        return sum
        


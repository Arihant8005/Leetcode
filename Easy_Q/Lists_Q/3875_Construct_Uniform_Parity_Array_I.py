# problem.: Given an array of distinct integers, determine whether it is possible to construct another array where
# all elements have the same parity (all odd or all even) using the allowed operations.

# Approach:
# Check the parity of the elements in nums1.
# Use the allowed subtraction operation to change parity when possible.
# Determine whether all elements can be made uniformly odd or even.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
# problem.136 : Single number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Approach :
# Traverse the array once and XOR every element with ans, so that all duplicate numbers cancel each other out,
# leaving only the unique number.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans


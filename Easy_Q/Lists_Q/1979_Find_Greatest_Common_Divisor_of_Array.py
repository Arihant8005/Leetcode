# problem.1979: Given an integer array nums, return the greatest common divisor of the
# smallest number and largest number in nums.

# Approach:
# Traverse the array to find the smallest and largest elements, then return their greatest common divisor.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List
from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max = min = nums[0]
        for val in nums:
            if(val > max):
                max = val
            if(val < min):
                min = val

        return gcd(min, max)

        
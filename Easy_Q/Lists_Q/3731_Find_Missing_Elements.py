# problem.3731: Given an integer array nums containing distinct values, return all the integers that are missing
# between the smallest and largest values in the array.

# Approach:
# Find the smallest and largest values, iterate through their range, and add each number that is not present in nums to the result.

# Time complexity: O(n × r)
# n is the length of nums.
# r is the range from the smallest to the largest value.
# val in nums takes O(n) in the worst case for each value.

# Space complexity: O(r)
# The result list can contain up to r missing elements.

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        list_missing = []

        smallest = min(nums)
        largest = max(nums)

        for val in range(smallest, largest + 1):
            if val in nums:
                continue
            else:
                list_missing.append(val)

        return list_missing
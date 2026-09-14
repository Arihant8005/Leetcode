# problem.448: Given an array nums containing numbers from 1 to n, where some numbers appear twice and others once, return all the numbers from 1 to n that do not appear in the array.

# Approach:
# Convert nums into a set for fast lookup.
# Check every number from 1 to n.
# If a number is not in the set, add it to result.
# Return the missing numbers.

# Time Complexity: O(n)
# Space Complexity: O(n) — for the set and result list.

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        my_set = set(nums)
        n = len(nums)
        for i in range(1, n+1):
            if i not in my_set:
                result.append(i)
        return result
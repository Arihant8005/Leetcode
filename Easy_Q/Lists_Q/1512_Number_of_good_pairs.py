# problem.1512: Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Approach:
# Check every pair of elements in the array using two nested loops, and increment the count whenever two elements are equal.

# Time Complexity: O(n²)
# Space Complexity: O(1)                   

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] == nums[j]):
                    count += 1

        return count
# problem.1 : Two sum
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Approach: 
# Traverse every possible pair of elements using two nested loops, and return the indices of the pair whose sum equals the target.

# Time Complexity: O(n²)
# Space Complexity: O(1)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
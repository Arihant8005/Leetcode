# problem.2089: Given an integer array nums and a target, sort nums in increasing order and return all indices where target appears.

# Approach:
# Sort nums in ascending order.
# Traverse the sorted array.
# If nums[i] == target, add index i to result.
# Return the result.

# Time Complexity: O(n log n) — due to sorting.
# Space Complexity: O(1) — excluding the output list.

from typing import List

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] == target):
                result.append(i)
        return result
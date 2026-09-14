# problem.442: Given an array nums where each integer appears once or twice, return all integers that appear twice.
# without using any extra space excluding output list

# Approach:
# Use the index marking technique.
# For each number, use abs(num) - 1 as its index.
# If nums[index] is already negative, the number has appeared before, so add it to result.
# Otherwise, make nums[index] negative to mark it as visited.

# Time Complexity: O(n)
# Space Complexity: O(1) — excluding the output list.

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]

        return result
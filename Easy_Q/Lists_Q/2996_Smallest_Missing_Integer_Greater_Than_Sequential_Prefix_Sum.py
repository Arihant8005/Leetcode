# problem.2996: Given an array nums, find the smallest integer that is greater than or equal to the sum of the longest consecutive
# prefix of nums, where consecutive elements increase by exactly 1, and that integer does not appear in nums.

# Approach:
# Find the sum of the longest consecutive prefix, then repeatedly increment it while it exists in nums.

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        result = nums[0]

        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1] + 1):
                result += nums[i]
            else:
                break
        while result in set(nums):
            result += 1
        return result
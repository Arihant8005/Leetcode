# problem.2239: Given an integer array nums, find the number closest to zero. If two numbers have the same distance from zero, return the positive number.

# Approach:
# Start with the first element as closest.
# Traverse the array and compare absolute values.
# Update closest if the current number is closer to zero.
# If positive and negative values have the same distance, return the positive one.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]

        for i in range(len(nums)):
            
            if(abs(nums[i]) < abs(closest)):

                closest = nums[i]
        
        if(closest < 0 and abs(closest) in nums):
            return abs(closest)
            
        return closest
    
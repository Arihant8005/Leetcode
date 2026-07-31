# problem.283: Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

# Approach :
# Use a pointer (start) to track the next position for a non-zero element and
# swap each non-zero element into that position while traversing the array once.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[start]
                nums[start] = nums[i]
                nums[i] = temp
                start = start + 1
        
        return nums

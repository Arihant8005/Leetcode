# problem.26: 
# Given a sorted array nums, remove duplicates in-place so that each element appears only once. Return the number of unique elements.

# Approach:
# Use two pointers i and j.
# j scans the array.
# When nums[j] != nums[i], move i forward and copy nums[j] to nums[i].
# Return i + 1.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 0):
            return 0
        i = 0
        for j in range(1,n):
            if(nums[j] != nums[i]):
                i += 1
                nums[i] = nums[j]
        return i+1

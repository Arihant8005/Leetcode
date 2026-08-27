# problem.1752: Given an array nums, check whether it is sorted in non-decreasing order and rotated some number of times.

# Approach
# Compare every element with the next element using (i + 1) % n.
# Count how many times nums[i] > nums[i+1].
# If the count is at most 1, return True; otherwise, return False.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if(nums[i] > nums[(i+1) % n]):
                count += 1
        return count <= 1
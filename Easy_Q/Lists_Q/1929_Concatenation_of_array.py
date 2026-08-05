# problem.1929: Given an integer array nums of length n, you want to create an array ans of length 2n
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n 

# Approach:
# Create a new array of size 2n, copy the elements of nums into the first half, 
# then copy them again into the second half.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = nums[i]

        for i in range(n):
            ans[i + n] = nums[i]

        return ans
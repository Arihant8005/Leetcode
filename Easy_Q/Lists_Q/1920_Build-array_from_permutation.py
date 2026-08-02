# problem.1920: Given a zero-based permutation nums (0-indexed), build an array ans of the same length 
# where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# Approach:
# Create a new array and, for each index, store the element found at the index specified by nums[i].

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans =[0] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans
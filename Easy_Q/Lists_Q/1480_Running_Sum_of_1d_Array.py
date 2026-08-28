# problem.1480: Given an array nums, return its running sum, where each element is the sum of all previous elements including itself.

# Approach:
# Maintain a variable sum.
# Traverse the array and keep adding each element to sum.
# Replace each element with the current sum.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums
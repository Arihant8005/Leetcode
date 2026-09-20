# problem.905: Given an integer array nums, move all even numbers to the beginning and all odd numbers to the end. The relative order does not need to be maintained.

# Approach:
# Use two pointers: i to traverse the array and j to track the next position for an even number.
# When nums[i] is even, swap it with nums[j].
# Increment j after placing the even number.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        j = 0
        for i in range(len(nums)):
            if(nums[i] % 2 == 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
# problem.414: Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist,
# return the maximum number.

# Approach:
# Maintain max1, max2, and max3 for the three largest distinct values, update them whenever a larger distinct number is found, and return max3 if it exists; otherwise return max1.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        for i in range(len(nums)):
            if(nums[i] > max1):
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif(nums[i] > max2 and nums[i] != max1):
                max3 = max2
                max2 = nums[i]
            elif(nums[i] > max3 and nums[i] != max1 and nums[i] != max2):
                max3 = nums[i]
        if max3 in nums:
            return max3
        else:
            return max1
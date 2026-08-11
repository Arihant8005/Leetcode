# problem.1365:Given an integer array nums, for each element, count how many numbers in the array are strictly smaller than it.
# Return the resulting array.

# Approach:
# For each element, traverse the entire array, count the elements smaller than it, and store that count at the same index.

# Time Complexity: O(n²)
# Space Complexity: O(n)

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_num = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] > nums[j]):
                    count_num[i] += 1

        return count_num
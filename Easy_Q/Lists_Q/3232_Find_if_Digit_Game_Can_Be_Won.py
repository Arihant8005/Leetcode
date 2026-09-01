# problem.3232: Given an array nums, Alice wins if the sum of all single-digit numbers is different from the sum of all double-digit numbers. Return whether Alice wins.

# Approach:
# Traverse the array.
# Add numbers less than 10 to s_sum.
# Add numbers greater than or equal to 10 to d_sum.
# Return whether the two sums are different.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s_sum = 0
        d_sum = 0
        for val in nums:
            if(val < 10):
                s_sum += val
            else:
                d_sum += val
        return (s_sum != d_sum)
# problem.3452: Given an integer array nums and an integer k, an element nums[i] is good if it is strictly greater than the elements at
# indices i-k and i+k, whenever those indices exist. Return the sum of all good elements.

# Approach:
# Traverse the array and skip an element if either existing neighbor at distance k is greater than or equal to it; otherwise, add it to the sum.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum_good = 0
        n = len(nums)

        for i in range(n):
            if i - k >= 0 and nums[i] <= nums[i - k]:
                continue


            if i + k < n and nums[i] <= nums[i + k]:
                continue

            sum_good += nums[i]

        return sum_good
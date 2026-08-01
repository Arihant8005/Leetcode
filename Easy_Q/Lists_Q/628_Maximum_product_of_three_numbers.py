# problem.628: Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Approach:
# Traverse the array once to track the three largest and two smallest numbers, 
# then return the maximum of their possible products.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            # Three largest
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            # Two smallest
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3,
                   max1 * min1 * min2)
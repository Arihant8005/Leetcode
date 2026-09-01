# problem.1822: Given an array nums, return the sign of the product of all its elements without calculating the actual product.

# Approach:
# If any element is 0, return 0.
# Count the negative numbers.
# If the count of negative numbers is even, return 1; otherwise, return -1.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count_neg = 0
        for val in nums:
            if(val == 0):
                return 0
            elif(val < 0):
                count_neg += 1
        
        return 1 if count_neg % 2 == 0 else -1
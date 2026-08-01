# problem.1295: Given an array nums of integers, return how many of them contain an even number of digits.

# Approach:
# Traverse each number, count its digits using repeated division by 10, and increment the answer if the digit count is even.

# Time Complexity: O(n * d)
# n = number of elements in nums
# d = number of digits in each number
# Space complexity: O(1)

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0

        for val in nums:
            count = 0
            temp = val

            while temp > 0:
                temp //= 10
                count += 1

            if count % 2 == 0:
                even_count += 1

        return even_count
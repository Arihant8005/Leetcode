# problem.2535: Find the difference between the sum of all elements and the sum of all digits of the elements.

# Approach:
# x = sum(nums) gives the sum of all numbers.
# Traverse each number and extract its digits using:
# val % 10 → last digit
# val //= 10 → remove last digit
# Store the total digit sum in y.
# Return abs(x - y).

# Time Complexity: O(n × d), where d is the number of digits.
# Space Complexity: O(1).

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = sum(nums)
        y = 0
        for val in nums:
            while(val > 0):
                rem = val % 10
                y += rem
                val //= 10
        return abs(x - y)
            
# problem.1837: Given an integer n and a base k, convert n into base k and return the sum of its digits.

# Approach:
# Repeatedly find the remainder when dividing n by k.
# Add the remainder to total.
# Divide n by k until it becomes 0.

# Time Complexity: O(logₖ n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while(n > 0):
            rem = n % k
            total += rem
            n //= k
        return total

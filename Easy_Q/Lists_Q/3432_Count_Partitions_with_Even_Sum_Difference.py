# problem.3432: Count the number of ways to split nums into two non-empty parts such that the absolute difference between their sums is even.

# Approach:
# First, calculate the total sum of all elements.
# For any partition:
# left_sum + right_sum = total_sum
# difference = left_sum - right_sum
# Rewrite the difference:
# difference = 2 × left_sum - total_sum
# 2 × left_sum is always even, so the difference will be even only when total_sum is even.
# Therefore:
# If total_sum is even → all n-1 partitions are valid.
# If total_sum is odd → no partition is valid.
# So we simply check the parity of the total sum.

# Time: O(n)
# Space: O(1)

from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)

        if total % 2 == 0:
            return len(nums) - 1

        return 0
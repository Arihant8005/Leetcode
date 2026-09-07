# problem.3427: For every index i, consider the subarray ending at i with length nums[i] + 1 (or starting from index 0 if that goes outside the array). Return the sum of all such subarrays.

# Approach:
# For each index i, calculate the starting index:
# start = max(0, i - nums[i])
# Traverse from start to i.
# Add all elements in this range to total.

# Time Complexity: O(n²) in the worst case.
# Space Complexity: O(1).

from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            start = max(0, i - nums[i])
            for j in range(start, i+1):
                total += nums[j]
        return total
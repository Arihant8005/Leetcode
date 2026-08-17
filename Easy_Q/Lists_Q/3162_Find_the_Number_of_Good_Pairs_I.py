# problem.3162: You are given two integer arrays nums1 and nums2, and an integer k. Count the number of pairs (i, j)such that nums1[i] is divisible by nums2[j] * k.

# Approach:
# Use two nested loops to check every possible pair and increment the count when nums1[i] % (nums2[j] * k) == 0.

# Time complexity: O(n × m)
# Space complexity: O(1)

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        count = 0


        for i in range(n):
            for j in range(m):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1


        return count
# problem.3131: Given two arrays nums1 and nums2, where every element in nums2 is obtained by adding the same integer x to the corresponding element of nums1, find x.

# Approach:
# Find the minimum element of both arrays.
# Since the same value x is added to every element:
# x = min(nums2) - min(nums1).
# Return the difference.

# Time Complexity: O(n + m)
# Space Complexity: O(1)


from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        Min1 = min(nums1)
        Min2 = min(nums2)

        return Min2 - Min1
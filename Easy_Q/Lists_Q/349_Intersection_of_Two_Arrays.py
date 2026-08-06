# problem.349: Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# Approach:
# Traverse nums1, add the elements that are also present in nums2 to a list,
# then remove duplicates using a set.

# Time Complexity: O(n × m)
# Space Complexity: O(n)

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for val in nums1:
            if val in nums2:
                intersection.append(val)
        unique = list(set(intersection))
        return unique
 
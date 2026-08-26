# problem.2215: Given two arrays nums1 and nums2, find:
# Elements present in nums1 but not in nums2.
# Elements present in nums2 but not in nums1.
# Return both lists.

# Approach:
# Convert both arrays into sets.
# Use set difference n1 - n2 and n2 - n1.
# Return the two resulting lists.

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)


from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        final = [0] * 2
        final[0] = list(n1 - n2)
        final[1] = list(n2 - n1)
        return final

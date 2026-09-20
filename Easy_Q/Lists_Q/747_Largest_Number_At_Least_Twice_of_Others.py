# problem.747: Given an integer array nums, find the index of the largest element if it is at least twice every other element. Otherwise, return -1.

# Approach:
# Keep track of the largest (L1) and second largest (L2) elements.
# Store the index of the largest element.
# After traversing, check whether L1 >= 2 × L2.
# If true, return the largest element's index; otherwise return -1.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        L1 = L2 = float("-inf")
        for i, val in enumerate(nums):
            if(val > L1):
                L2 = L1
                L1 = val
                index = i
            elif(val > L2):
                L2 = val

        return index if(L1 >= L2 * 2) else -1


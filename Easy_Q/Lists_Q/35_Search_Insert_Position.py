# problem.35: Given a sorted array nums and a target, return the index of the target. If the target is not present, return the index where it should be inserted to maintain sorted order.

# Approach:
# Use binary search with low and high.
# If nums[mid] == target, return mid.
# If nums[mid] >= target, store mid as the possible insertion position and search left.
# Otherwise, search right.
# Return Lb after the search.

# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        n = len(nums)
        low = 0
        high = n - 1
        Lb = n
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] >= target):
                high = mid - 1
                Lb = mid
            else:
                low = mid + 1
        return Lb
        

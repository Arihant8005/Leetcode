# problem.34: Given a sorted array nums and a target, find the first and last positions of the target. If the target is not present, return [-1, -1].

# Approach:
# Use Lower Bound to find the first occurrence of target.
# If target is not present at that index, return [-1, -1].
# Use Upper Bound to find the first element greater than target.
# The last occurrence is upper_bound - 1.

# Time Complexity: O(log n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        L_val = self.lower_bound(nums, target)
        if(L_val == -1 or nums[L_val] != target):
            return [-1, -1]
        U_val = self.upper_bound(nums, target)
        return [L_val, U_val - 1]
    

    def lower_bound(self, nums, target):
        low = 0
        high = len(nums) - 1
        LB = -1
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] >= target):
                LB = mid
                high = mid - 1
            else:
                low = mid + 1

        return LB

    def upper_bound(self, nums, target):
        low = 0
        high = len(nums) - 1
        UB = len(nums)
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] > target):
                UB = mid
                high = mid - 1
            else:
                low = mid + 1

        return UB
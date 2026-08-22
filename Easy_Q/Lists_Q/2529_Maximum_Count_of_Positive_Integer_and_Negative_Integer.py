# problem.2529: Given a sorted array nums, find the maximum count between positive numbers and negative numbers. Ignore zeros.

# Approach:
# Traverse the array.
# Count negative numbers in neg and positive numbers in pos.
# Ignore zeros.
# Return max(pos, neg).

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for val in nums:
            if(val < 0):
                neg += 1
            elif(val > 0):
                pos += 1
            else:
                continue
        return max(pos, neg)
# problem.485: Given a binary array nums, find the maximum number of consecutive 1s.

# Approach:
# Traverse the array and count consecutive 1s.
# When a 0 appears, update the maximum count and reset the current count.
# Return the maximum count.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for val in nums:
            if(val == 1):
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(count,max_count)
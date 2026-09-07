# problem.1470: Given an array nums of length 2n, rearrange it in the form:
# [x1, y1, x2, y2, ..., xn, yn]
# where the first n elements are x values and the last n elements are y values.

# Approach:
# Create an empty result list.
# Loop from 0 to n-1.
# Add nums[i] from the first half.
# Add nums[i+n] from the second half.
# Return result.

# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result



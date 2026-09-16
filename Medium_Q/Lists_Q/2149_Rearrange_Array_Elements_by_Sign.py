# problem.2149: Rearrange the array so that positive and negative numbers appear alternately, starting with a positive number, while maintaining their relative order.

# Approach:
# Create a result array of the same size.
# Keep pos_idx at even indices (0, 2, 4...) for positive numbers.
# Keep neg_idx at odd indices (1, 3, 5...) for negative numbers.
# Traverse nums and place each number at its corresponding index.

# Time Complexity: O(n)
# Space Complexity: O(n) — for the result array.

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos_idx, neg_idx = 0, 1
        for val in nums:
            if(val > 0):
                result[pos_idx] = val
                pos_idx += 2
            else:
                result[neg_idx] = val
                neg_idx += 2
        return result
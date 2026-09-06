# problem.3903: Find the first stable index i where the difference between the maximum value in nums[0...i] and the minimum value in nums[i...n-1] is at most k.

# Approach:
# Create min_suffix to store the minimum value from each index to the end.
# Traverse the array while maintaining max_prefix, the maximum value from the start to the current index.
# Calculate:
# instability_score = max_prefix - min_suffix[i]
# If this score is <= k, return i.
# If no such index exists, return -1.

# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # min_suffix[i] stores the minimum value in nums[i..n-1]
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])
        
        max_prefix = float("-inf")
        
        for i in range(n):
            max_prefix = max(max_prefix, nums[i])
            instability_score = max_prefix - min_suffix[i]
            
            if instability_score <= k:
                return i
                
        return -1
           
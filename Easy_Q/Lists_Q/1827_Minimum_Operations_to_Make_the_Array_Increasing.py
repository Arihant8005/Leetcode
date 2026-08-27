# problem.1827: Given an array nums, make it strictly increasing using the minimum number of increment operations.
# In one operation, increase an element by 1.

# Approach
# Traverse the array from left to right.
# If nums[i] >= nums[i+1], increase nums[i+1] until it becomes greater than nums[i].
# Add the required increments to count_op.
# Return the total operations.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_op = 0
        n = len(nums)
        for i in range(n-1):
            if(nums[i] >= nums[i+1]):
                operations = nums[i] - nums[i+1] + 1
                count_op += operations
                nums[i+1] += operations
        
        return count_op
# problem.3550: Find the smallest index i such that the sum of digits of nums[i] equals i. If no such index exists, return -1.

# Approach:
# Traverse nums using enumerate() to get both index i and value val.
# Calculate the sum of digits using % 10 and // 10.
# If total == i, return the current index.
# If no index satisfies the condition, return -1.

# Time Complexity: O(n × d), where d is the number of digits in each number.
# Space Complexity: O(1).


from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i , val in enumerate(nums):
            total = 0
            while(val > 0):
                rem = val % 10
                total += rem
                val //= 10
            if(total == i):
                return i
        return -1
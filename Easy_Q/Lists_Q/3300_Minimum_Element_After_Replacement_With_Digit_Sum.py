# problem.3300: For each element in nums, calculate the sum of its digits. Return the minimum digit sum among all elements.

# Approach:
# Traverse every element of nums.
# Extract each digit using % 10.
# Add the digits together.
# Replace the original number with its digit sum.
# Finally, return the minimum value using min(nums).

# Time Complexity
# O(n × d), where d is the number of digits in a number.
# Space Complexity: O(1)


from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            sum = 0
            val = nums[i]
            while(val > 0):
                rem = val % 10
                sum = sum + rem
                val //= 10
            nums[i] = sum
        return min(nums)
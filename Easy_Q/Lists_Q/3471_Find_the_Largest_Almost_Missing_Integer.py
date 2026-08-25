# problem.3471: Given an array nums and an integer k, find the largest integer that appears in exactly one subarray of size k. 
# Return -1 if no such integer exists.

# Approach:
# Generate every subarray of size k.
# Use a set so a number is counted only once per subarray.
# Store how many subarrays contain each number.
# Return the largest number with frequency 1.
    
# Time Complexity: O(n × k)
# Space Complexity: O(n)



from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        for i in range(len(nums) - k + 1):
            subarray = set(nums[i:i + k])

            for num in subarray:
                count[num] = count.get(num, 0) + 1

        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans
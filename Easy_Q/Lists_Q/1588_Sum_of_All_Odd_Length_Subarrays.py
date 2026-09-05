# problem.1588 :Given an array arr, find the sum of all odd-length subarrays.

# Approach:
# Start each subarray at index i.
# Extend it using j while maintaining its running sum.
# If the subarray length is odd, add its sum to ans.

# Time Complexity: O(n²)
# Space Complexity: O(1)

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]
                length = j - i + 1
                if(length % 2 == 1):
                    ans += total
        return ans
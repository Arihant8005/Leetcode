# problem.1732: Given an array gain where gain[i] represents the altitude change between two points, find the highest altitude reached. The starting altitude is 0.

# Approach:
# Start with altitude 0.
# Keep adding each gain[i] to total.
# Store each altitude in result.
# Return the maximum altitude.

# Time Complexity: O(n)
# Space Complexity: O(n) — for the result list.

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        total = 0
        for i in range(len(gain)):
            total += gain[i]
            result.append(total)
        return max(result)
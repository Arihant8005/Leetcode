# problem.1299: Replace every element in the array with the greatest element among the elements to its right. The last element is replaced with -1.

# Approach:
# Traverse the array from right to left.
# Keep right as the maximum element seen so far.
# Replace arr[i] with right.
# Update right using the original value of arr[i].

# Time Complexity: O(n)
# Space Complexity: O(1) — done in-place.


from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = right
            right = max(right, current)
        return arr
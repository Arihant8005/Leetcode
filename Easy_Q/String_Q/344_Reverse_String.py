# problem.344: Given an array of characters s, reverse the string in-place.

# Approach:
# Use two pointers: i at the start and j at the end.
# Swap s[i] and s[j].
# Move i forward and j backward until they meet.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while(i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1

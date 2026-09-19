# problem.1528: Given a string s and an array indices, rearrange the characters of s so that each character is placed at the position specified by indices[i].

# Approach:
# Create an empty array restore of the same length as s.
# For each character, place s[i] at index indices[i].
# Join the array to form the restored string.
# Time Complexity: O(n)
# Space Complexity: O(n) — for the restore array.

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restore = [""] * len(indices)
        for i in range(len(indices)):
            restore[indices[i]] = s[i]
        return "".join(restore)
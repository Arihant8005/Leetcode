# problem.2586: Count the number of strings in words[left...right] that start and end with a vowel (a, e, i, o, u).

# Approach:
# Loop from left to right.
# Check whether the first and last character are vowels.
# If both are vowels, increment count.
# Return count.

# Time Complexity: O(n), where n = right - left + 1.
# Space Complexity: O(1).

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = "aeiou"
        for i in range(left, right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count
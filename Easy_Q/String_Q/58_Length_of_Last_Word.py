# problem.58: Given a string s containing words and spaces, return the length of the last word.

# Approach:
# Start from the end and skip trailing spaces.
# Count characters until a space or the beginning of the string is reached.
# Return the count.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        count = 0
        i = length - 1
        while(i >=0 and s[i] == ' '):
            i -= 1
        while(i >= 0 and s[i] != ' '):
            i -= 1
            count += 1

        return count

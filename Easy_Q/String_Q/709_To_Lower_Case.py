# problem.709: Given a string s, convert all uppercase English letters to lowercase and return the resulting string.

# Approach:
# Traverse each character of the string.
# If the character is between 'A' and 'Z', convert it using:
# chr(ord(ch) + 32).
# Otherwise, keep it unchanged.
# Add each character to ans.

# Time Complexity: O(n)
# Space Complexity: O(n) — for the output string.

from typing import List

class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                ans += chr(ord(ch) + 32)
            else:
                ans += ch

        return ans
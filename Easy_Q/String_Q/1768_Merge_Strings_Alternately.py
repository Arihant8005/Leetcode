# problem.1768: Given two strings word1 and word2, merge them by taking characters alternately from each string. If one string is longer, append its remaining characters at the end.

# Approach:
# Loop up to the length of the longer string.
# Add the character from word1 if available.
# Add the character from word2 if available.
# Join the characters to form the final string.

# Time Complexity: O(n + m)
# Space Complexity: O(n + m) — for the output list.

from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1),len(word2))
        output = []
        for i in range(n):
            if(i < len(word1)):
                output.append(word1[i])
            if(i < len(word2)):
                output.append(word2[i])
            
        return "".join(output)
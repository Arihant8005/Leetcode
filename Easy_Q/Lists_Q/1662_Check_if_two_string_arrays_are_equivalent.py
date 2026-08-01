# problem.1662: Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# Approach:
# Join all strings in both arrays into two complete strings and compare them for equality.

# Time Complexity: O(n + m)
# n = total length of all strings in word1
# m = total length of all strings in word2
# Space Complexity: O(n + m)

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(word1)
        s2 = "".join(word2)

        if s1 == s2:
            return True
        else:
            return False
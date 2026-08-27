# problem.1816 : Given a sentence s and an integer k, return the sentence containing only the first k words.

# Approach
# Split the sentence into words.
# Take the first k words.
# Join them back into a sentence.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1 = s.split()
        
# problem.2828: Given a list of words and a string s, check whether s is the acronym formed by the first letter of each word.

# Approach:
# Traverse through words.
# Take the first character of each word and add it to letter.
# Compare letter with s.
# Return True if they are equal, otherwise False.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        letter = ""
        for i in range(len(words)):
            letter += words[i][0]

        return letter == s
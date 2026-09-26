# problem.1961: Given a string s and an array words, check whether s can be formed by concatenating a prefix of words.

# Approach:
# Start with an empty string res.
# Traverse words and keep adding each word to res.
# If res == s, return True.
# If the loop finishes without matching s, return False.

# Time Complexity: O(n) — where n is the total number of characters processed.
# Space Complexity: O(n) — for the concatenated string res.

from typing import List

class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        n = len(s)
        res = ""
        
        for val in words:
            res += val
            if(res == s):
                return True
        return False
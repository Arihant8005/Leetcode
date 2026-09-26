# problem.2255: Given a list of strings words and a string s, count how many strings in words are prefixes of s.

# Approach:
# Build the prefix of s character by character.
# For each prefix, use words.count() to check how many times it appears in words.
# Add that count to cnt.
# Return cnt.

# Time Complexity: O(n × m) — where n is the length of s and m is the number of words.
# Space Complexity: O(n) — for the prefix string res.

class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        cnt = 0
        res = ""
        for ch in s:
            res += ch
            cnt += words.count(res)
        return cnt




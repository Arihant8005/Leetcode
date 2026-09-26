# problem.28: Given two strings haystack and needle, find the first occurrence of needle in haystack. Return its index, or -1 if it doesn't exist.

# Approach:
# Traverse haystack from left to right.
# At each index, take a substring of length needle.
# Compare it with needle.
# If they match, return the current index.
# If no match is found, return -1.

# Time Complexity: O(n × m) — where n is the length of haystack and m is the length of needle.
# Space Complexity: O(m) — for the substring created during comparison.


from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if(haystack[i: i + len(needle)] == needle):
                return i
        return -1
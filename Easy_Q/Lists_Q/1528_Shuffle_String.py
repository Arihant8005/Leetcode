# problem.1528: Given a string s and an integer array indices, rearrange the characters of s so that 
# the character at index i is placed at position indices[i]. Return the restored string.

# Approach:
# Create a result list, place each character at its required index using indices, and join the list to form the final string.

# Time complexity: O(n)
# Space complexity: O(n)


from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restore = [""] * len(indices)


        for i in range(len(indices)):
            restore[indices[i]] = s[i]


        return "".join(restore)
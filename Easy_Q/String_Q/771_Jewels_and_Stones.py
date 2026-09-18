# problem.771: Given two strings jewels and stones, count how many characters in stones are also present in jewels.

# Approach:
# Store all jewel characters in a set.
# Traverse through stones.
# If a stone is present in the set, increment count.
# Return the count.

# Time Complexity: O(n + m)
# Space Complexity: O(n) — for the set of jewels.

from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n1 = len(jewels)
        n2 = len(stones)
        count = 0

        for i in range(n1):
            for j in range(n2):
                if(jewels[i] == stones[j]):
                    count += 1
        return count

# problem.877: There are an even number of piles of stones. In each turn, Alice and Bob take one pile from either end. Alice goes first. Both play optimally. Return True if Alice can win.

# Approach:
# The key observation is that the number of piles is even.
# Alice can always choose either all piles at even indices or all piles at odd indices.
# She chooses the group whose total sum is larger.
# Therefore, Alice can always collect more stones than Bob.

# Time Complexity: O(1)
# Space Complexity: O(1)


from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

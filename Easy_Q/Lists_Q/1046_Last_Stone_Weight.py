# problem.1046: You are given an array stones where each value represents the weight of a stone. 
# Repeatedly choose the two heaviest stones and smash them together:
# If they have the same weight, both are destroyed.
# If they have different weights, the heavier stone is reduced by the lighter stone's weight.
# Return the weight of the remaining stone, or 0 if no stones remain.

# Approach:
# Find the two largest stones in each round, remove them, and append their difference until at most one stone remains.

# Time Complexity: O(n²)
# Space Complexity: O(1)

from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            max1 = max2 = -1
            for i in range(len(stones)):
                if(stones[i] > max1):
                    max2 = max1
                    max1 = stones[i]
                elif(stones[i] > max2):
                    max2 = stones[i]
            if(max1 != max2):
                stones.remove(max1)
                stones.remove(max2)
                stones.append(max1 - max2)
            else:
                stones.remove(max1)
                stones.remove(max2)
        if(stones):
            return stones[0]
        else:
            return 0

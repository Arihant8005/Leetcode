# problem.575: You are given an array candyType representing the types of candies. You can eat only half of the candies and 
# want to eat the maximum number of different candy types. Return the maximum number of different types you can eat.

# Approach:
# The answer is the smaller of half the total candies and the number of unique candy types.

# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
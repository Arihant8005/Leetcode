# problem.1431: Given an array candies representing the number of candies each child has and an integer extraCandies
# ,determine whether each child can have the greatest number of candies after receiving all the extra candies.

# Approach:
# Find the current maximum number of candies, then check for each child whether candies[i] + extraCandies is at least the maximum.

# Time Complexity: O(n)
# space complexity: O(n)

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        true_list = [True] * len(candies)
        greatest = max(candies)

        for i in range(len(candies)):
            candies[i] += extraCandies
            if(candies[i] < greatest):
                true_list[i] = False

        return true_list
# problem.1346: Given an array arr of integers, check if there exist two indices i and j such that :
# i != j and 0 <= i, j < arr.length and arr[i] == 2 * arr[j]

# Approach:
# First check whether there are at least two zeros, then compare every pair of distinct elements to check if one is twice the other.

# Time complexity: O(n²)
# Space complexity: O(1)

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        if (arr.count(0) >= 2):
            return True
        for i in range(n):
            for j in range(n):
                if(arr[i] == 2 * arr[j] and i != j):
                    return True
                
        return False
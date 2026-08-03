# problem.1534: Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length|arr[i] - arr[j]| <= a and |arr[j] - arr[k]| <= b and |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.

# Approach:
# Check every possible triplet (i, j, k) such that i < j < k, and count the triplets
# whose absolute differences satisfy all three given conditions.

# Time Complexity: O(n³)
# Space Complexity: O(1)

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if(abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c):
                        count += 1
        return count
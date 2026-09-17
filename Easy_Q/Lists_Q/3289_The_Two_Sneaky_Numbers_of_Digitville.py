# problem.3289: Given an array nums containing numbers from 0 to n-1, where exactly two numbers appear twice, return those two repeated numbers.

# Approach:
# Use a dictionary dist to store the frequency of each number.
# Traverse the array and increase its frequency.
# When a number's frequency becomes 2, add it to result.
# Return the repeated numbers.

# Time Complexity: O(n)
# Space Complexity: O(n) — for the dictionary.


from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        dist = {}
        for val in nums:
            dist[val] = dist.get(val, 0) + 1
            if(dist[val] == 2):
                result.append(val)
        return result
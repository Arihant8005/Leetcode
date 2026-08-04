# problem.66: You are given a large integer represented as an array of digits, 
# where each element contains a single digit and the digits are arranged from most significant 
# to least significant. Increment the integer by one and return the resulting array of digits.

# Approach:
# Convert the array of digits into an integer, add 1, then convert the result back into an array of digits.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list_plus = []
        interger = "".join(map(str,digits))
        integer_plus = int(interger) + 1
        for val in str(integer_plus):
            list_plus.append(int(val))
        
        return list_plus

# problem.2011: Initially, the value of X is 0.
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

# Approach:
# raverse all operations and update x based on whether the operation is an increment (++) or decrement (--).

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for val in operations:
            if(val == '++X'  or val == 'X++'):
                x += 1
            else:
                x -= 1
        return x
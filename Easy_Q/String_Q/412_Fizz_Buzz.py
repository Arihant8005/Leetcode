# problem.412: Given an integer n, return a list from 1 to n where:
# Multiples of 3 → "Fizz"
# Multiples of 5 → "Buzz"
# Multiples of both → "FizzBuzz"
# Otherwise → the number as a string.

# Approach:
# Loop from 1 to n.
# Check divisibility by both 3 and 5 first.
# Then check 5, then 3.
# Otherwise, append the number as a string.

# Time Complexity: O(n)
# Space Complexity: O(n) — for the output list.

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if(i % 3 == 0 and i % 5 == 0):
                answer.append('FizzBuzz')
            elif(i % 5 == 0):
                answer.append('Buzz')
            elif(i % 3 == 0):
                answer.append('Fizz')
            else:
                answer.append(str(i))
        
        return answer
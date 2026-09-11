# problem.2094: Find all unique 3-digit even numbers that can be formed using the digits in digits.

# Approach:
# Create freq to store how many times each digit appears.
# Check every 3-digit even number from 100 to 998.
# Extract its three digits:
# a → hundreds
# b → tens
# c → units
# Temporarily decrease the frequencies of a and b to ensure the same digit isn't used more times than available.
# If c is available, add the number to result.
# Restore the frequencies afterward.

# Time Complexity: O(n + 900) → effectively O(n)
# Space Complexity: O(1) — freq always has only 10 elements.

from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10

        result = []
        for val in digits:
            freq[val] += 1
        
        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            if(freq[a] > 0):
                freq[a] -= 1

                if(freq[b] > 0):
                    freq[b] -= 1

                    if(freq[c] > 0):
                        result.append(num)

                    freq[b] += 1

                freq[a] += 1
        
        return result
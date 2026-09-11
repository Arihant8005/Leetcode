# problem.3483: Given an array of digits, count how many unique 3-digit even numbers can be formed using the given digits. A digit can only be used as many times as it appears in the array.

# Approach:
# Store the frequency of each digit.
# Check every 3-digit even number from 100 to 998.
# Extract its three digits and check whether they are available in the frequency array.
# Temporarily reduce frequencies to handle duplicate digits correctly.
# Count every valid number.

# Time Complexity: O(n) — checking the fixed 450 possible 3-digit even numbers is constant time.
# Space Complexity: O(1) — frequency array has only 10 elements.

from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for val in digits:
            freq[val] += 1
        
        count = 0
        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            if(freq[a] > 0):
                freq[a] -= 1

                if(freq[b] > 0):
                    freq[b] -= 1

                    if(freq[c] > 0):
                        count += 1
                    
                    freq[b] += 1
                
                freq[a] += 1
        
        return count
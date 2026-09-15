# problem.204: Given an integer n, count the number of prime numbers less than n.

# Approach:
# Use the Sieve of Eratosthenes.
# Create a boolean array where each index represents whether the number is prime.
# Start from 2 and mark all its multiples as non-prime.
# Continue up to √n.
# Finally, count the remaining True values.

# Time Complexity: O(n log log n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1

        return sum(is_prime)
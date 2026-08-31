# problem.2180: Given an integer num, count how many numbers from 1 to num have an even sum of digits.

# Approach:
# Traverse every number from 1 to num.
# Calculate the sum of its digits.
# If the digit sum is even, increase the count.
# Return the count.

# Time Complexity: O(n log n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num+1):
            sum = 0
            while(i > 0):
                rem = i % 10
                sum += rem
                i //= 10
            if(sum % 2 == 0):
                count += 1
        return count
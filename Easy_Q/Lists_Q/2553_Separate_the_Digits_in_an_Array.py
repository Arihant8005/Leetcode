# problem.2553: Given an array of positive integers nums, separate every digit of each number and return all digits in order.

# Approach:
# Traverse each number in nums.
# Convert the number to a string and iterate through its digits.
# Convert each digit back to an integer and add it to the result.

# Time Complexity: O(d) — where d is the total number of digits.
# Space Complexity: O(d) — for the result array.


from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            for ch in str(num):
                answer.append(int(ch))
        return answer
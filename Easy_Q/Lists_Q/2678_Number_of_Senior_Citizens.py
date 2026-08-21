# problem.2678: Given a list of strings containing passenger details, count how many passengers are older than 60 years.

# Approach:
# Traverse each passenger's detail string.
# Extract the age using val[-4:-2].
# If age > 60, increase count.
# Return count.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for val in details:
            if(int(val[-4:-2]) > 60):
                count += 1
        return count
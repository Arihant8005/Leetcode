# problem.1491: Find the average salary excluding the minimum and maximum salary.

# Approach:
# Find the maximum salary using max().
# Find the minimum salary using min().
# Traverse the array and add only salaries that are neither minimum nor maximum.
# Divide the total by len(salary) - 2.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = max(salary)
        min_salary = min(salary)

        total = 0
        for val in salary:
            if val != max_salary and val != min_salary:
                total += val

        return total / (len(salary) - 2)
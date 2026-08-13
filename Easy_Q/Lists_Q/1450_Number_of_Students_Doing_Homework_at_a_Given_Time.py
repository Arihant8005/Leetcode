# problem.1450: Given two integer arrays startTime and endTime, and an integer queryTime, 
# return the number of students who are doing their homework at queryTime.

# Approach:
# Traverse all students and count the students whose start time is at most queryTime and end time is at least queryTime.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1

        return count
# problem.682: You are given a list of operations representing a baseball game. Each operation can be:
# An integer → Add that score to the record.
# "+" → Add the sum of the previous two scores.
# "D" → Add double the previous score.
# "C" → Remove the previous score.
# Return the total score after performing all operations.

# Approach:
# Traverse each operation:"C" → remove the last score."D" → add double the last score."+" → add the sum of the last two scores.
# Otherwise → convert the operation to an integer and add it.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for val in operations:
            if(val == "C"):
                record.pop()
            elif(val == "D"):
                record.append(2 * record[-1])
            elif(val == "+"):
                record.append(record[-1] + record[-2])
            else:
                record.append(int(val))

        return sum(record)

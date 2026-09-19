# problem.1678: Given a command string containing "G", "()", and "(al)", interpret it as:
# "G" → "G"
# "()" → "o"
# "(al)" → "al"
# Return the interpreted string.

# Approach:
# Replace "()" with "o".
# Replace "(al)" with "al".
# Return the resulting string.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command
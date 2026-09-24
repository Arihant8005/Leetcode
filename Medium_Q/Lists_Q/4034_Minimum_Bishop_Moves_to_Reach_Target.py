# problem.4034: Given the starting position source and target position target of a bishop on a chessboard, find the minimum number of moves required to reach the target. Return -1 if it is impossible.

# Approach:
# A bishop always stays on the same color square.
# If (row + col) parity differs, return -1.
# If the source and target are on the same diagonal, return 1.
# Otherwise, any reachable target can be reached in 2 moves.

# Time Complexity: O(1)
# Space Complexity: O(1)

from typing import List

class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        sr, sc = source
        tr, tc = target

        if(sr + sc) % 2 != (tr + tc) % 2:
            return -1
        if(abs(sr - tr) == abs(sc - tc)):
            return 1

        return 2
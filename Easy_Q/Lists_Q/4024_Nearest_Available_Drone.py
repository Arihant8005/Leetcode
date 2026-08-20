# problem.4024: Given a list of drones where each drone is represented as [x, y, range], and a target [tx, ty], return the index
# of the nearest drone that can reach the target using Manhattan distance. If no drone can reach the target, return -1.

# Approach:
# Traverse all drones, calculate their Manhattan distance to the target, and update the answer whenever a reachable drone has a smaller distance.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        dist_min = float('inf')
        ans_idx = -1
        n = len(drones)


        for i in range(n):
            dist = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])

            if dist <= drones[i][2] and dist < dist_min:
                dist_min = dist
                ans_idx = i


        return ans_idx
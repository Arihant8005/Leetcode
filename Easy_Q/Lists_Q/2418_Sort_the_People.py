# problem.2418: You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n.Return names sorted in descending order by the people's heights.

# Approach:
# Create (height, name) pairs using zip(), sort them in descending order of height, and extract the names into the answer list.

# Time complexity: O(n log n)
# Space complexity: O(n)

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True)

        answer = []
        for height, name in people:
            answer.append(name)

        return answer
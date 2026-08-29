# problem.350: Given two arrays, return their intersection, including duplicate elements.

# Approach:
# Store the frequency of elements in nums2 using Counter.
# Traverse nums1.
# If an element exists in the frequency map, add it to the result and decrease its frequency.

# Time Complexity: O(n + m)
# Space Complexity: O(m)



from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = Counter(nums2)
        result = []

        for val in nums1:
            if freq[val] > 0:
                result.append(val)
                freq[val] -= 1
        
        return result
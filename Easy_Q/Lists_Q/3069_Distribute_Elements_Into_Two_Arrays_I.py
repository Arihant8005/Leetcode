# problem.3069: Given an array nums, split its elements into two arrays. The first two elements go into separate arrays. 
# For every next element, add it to the array whose last element is smaller. Finally, return both arrays combined.

# Approach:
# Put nums[0] in arr1 and nums[1] in arr2.
# Traverse from index 2.
# If arr1[-1] > arr2[-1], add the element to arr1; otherwise, add it to arr2.
# Return arr1 + arr2.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        j = 0
        k = 0
        for i in range(2,n):
            if(arr1[j] > arr2[k]):
                arr1.append(nums[i])
                j += 1
            else:
                arr2.append(nums[i])
                k += 1
        return arr1 + arr2
# problem.1464: Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Approach:
# Traverse the array once while keeping track of the largest and second largest elements. After the traversal,
# return the product of (largest - 1) and (second largest - 1).

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        max1 = max2 = -1
        for i in range(length):
            if(nums[i] > max1):
                max2 = max1
                max1 = nums[i]
            elif(nums[i] > max2):
                max2 = nums[i]

        return (max1-1)*(max2-1)
# problem.15: Given an integer array nums, find all unique triplets [a, b, c] such that:
# a + b + c = 0

# Approach:
# Sort the array.
# Fix one element using i.
# Use two pointers j and k to find the other two elements.
# Move j forward if the sum is less than 0, and k backward if the sum is greater than 0.
# When the sum is 0, add the triplet and skip duplicates.

# Time Complexity: O(n²)
# Space Complexity: O(1) — excluding the output list.

from typing import List

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if(i != 0 and nums[i] == nums[i - 1]):
                continue
            
            j = i + 1
            k = n - 1
            while(j < k):
                total = nums[i] + nums[j] + nums[k]
                if(total < 0):
                    j += 1
                elif(total > 0):
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    result.append(temp)
                    j += 1
                    k -= 1
                    while(j < k) and (nums[j] == nums[j - 1]):
                        j += 1
                    while(j < k) and (nums[k] == nums[k + 1]):
                        k -= 1
        
        return result


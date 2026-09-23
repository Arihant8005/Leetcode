# problem.18: Given an integer array nums and a target value, find all unique quadruplets [a, b, c, d] such that:
# a + b + c + d = target

# Approach:
# Sort the array.
# Use two loops to fix the first two elements.
# Use two pointers k and l to find the remaining two elements.
# Move pointers based on whether the sum is smaller or larger than target.
# Skip duplicate values to avoid duplicate quadruplets.

# Time Complexity: O(n³)
# Space Complexity: O(1) — excluding the output list.

from typing import List

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if(i != 0 and nums[i] == nums[i - 1]):
                continue
            
            for j in range(i+1, n):
                if(j != i + 1 and nums[j] == nums[j - 1]):
                    continue
                
                k = j + 1
                l = n - 1
                while(k < l):
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if(total < target):
                        k += 1
                    elif(total > target):
                        l -= 1
                    else:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        result.append(temp)
                        k += 1
                        l -= 1
                        while(k < l and nums[k] == nums[k - 1]):
                            k += 1
                        while(k < l and nums[l] == nums[l + 1]):
                            l -= 1
        
        return result


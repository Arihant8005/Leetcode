# problem.189: Rotate an array nums to the right by k steps in-place.

# Approach:
# First reverse the last k elements.
# Then reverse the first n-k elements.
# Finally reverse the entire array.
# This places all elements in their correct rotated positions without using extra space.

# Important: Use k %= n to handle k > n.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        
        k = k %  n
        if k == 0:
            return

        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
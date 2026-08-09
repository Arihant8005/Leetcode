# problem.832: You are given a binary matrix image containing only 0 and 1. Flip the image horizontally, then invert it by changing
# every 0 to 1 and every 1 to 0. Return the resulting image.

# Approach:
# Pair each height with its name, sort the pairs by height in descending order, and extract the names.

# Time Complexity: O(m × n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            start = 0
            end = len(image[0]) - 1
            while(start < end):
                image[i][start], image[i][end] = image[i][end], image[i][start]
                start += 1
                end -= 1
        
        for i in range(len(image)):
            start = 0
            while(start < len(image[0])):
                if(image[i][start] == 1):
                    image[i][start] = 0
                else:
                    image[i][start] = 1
                start += 1
        return image
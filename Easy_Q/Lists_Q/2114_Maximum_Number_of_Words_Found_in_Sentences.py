# problem.2114: Given an array of strings sentences, where each string represents a sentence, 
# return the maximum number of words found in any single sentence.

# Approach:
# Split each sentence into words, count the words, and keep track of the maximum count.

# Time Complexity: O(n × m)
# Space Complexity: O(m)

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in sentences:
            words = len(i.split())
            if(words > count):
                count = words
            
        return count
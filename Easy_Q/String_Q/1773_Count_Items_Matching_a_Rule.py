# problem.1773: Given a list of items, each with type, color, and name, count how many items match the given ruleKey and ruleValue.

# Approach:
# Map ruleKey to its corresponding index:
# "type" → 0
# "color" → 1
# "name" → 2
# Traverse all items.
# If items[i][index] == ruleValue, increment count.

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        outer_list = len(items)
        count = 0
        
        for i in range(outer_list):
                if(ruleKey == "type" and ruleValue == items[i][0]):
                    count += 1
                elif(ruleKey == "color" and ruleValue == items[i][1]):
                    count += 1
                elif(ruleKey == "name" and ruleValue == items[i][2]):
                    count += 1
        return count

                
                    
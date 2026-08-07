# problem.1773: You are given a list of items, where each item contains three properties: type, 
# color and name. Given a ruleKey and ruleValue, count how many items match the specified property and value.

# Approach:
# Traverse all items and increment the count whenever the property specified by ruleKey matches the given ruleValue.

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

                
                    
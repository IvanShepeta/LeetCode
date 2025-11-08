"""
------------------------------------------------------------
🧠 Problem: 1436. Destination City
🔗 Link: https://leetcode.com/problems/destination-city/
------------------------------------------------------------
📜 Description:
You are given a list of paths, where each path = [from, to].
Return the city that never appears as a starting point.

💡 Example:
Input:  paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"

🧩 Approach:
- Collect all starting cities into a set.
- The destination city is the one not in that set.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = {a for a, b in paths }
        for a, b in paths:
            if b not in start:
                return b
        return None


s = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

result = s.destCity(paths)

print(result)
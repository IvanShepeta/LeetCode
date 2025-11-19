"""
------------------------------------------------------------
🧠 Problem: 207. Course Schedule
🔗 Link: https://leetcode.com/problems/course-schedule/
------------------------------------------------------------
📜 Description:
You are given:
  - numCourses: total number of courses
  - prerequisites: list of pairs [a, b] meaning:
        To take course a, you must first take course b.

Return True if it's possible to finish all courses (i.e., no cycles).

💡 Example:
Input:
    numCourses = 2
    prerequisites = [[1, 0]]
Output:
    True

Input:
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
Output:
    False   (cycle)

🧩 Approach (DFS — Cycle Detection):
We treat courses as nodes of a directed graph.
Each pair [a, b] means:  b → a

We perform a DFS to detect cycles:
    - visitSet stores nodes in the current DFS path
    - If we enter a node already in visitSet → cycle → return False
    - After fully exploring a node, memoize it by clearing adjacency list

Steps:
1. Build adjacency list.
2. DFS each course.
3. If any DFS returns False → cycle → cannot finish.

⏱️ Time Complexity:  O(V + E)
💾 Space Complexity: O(V + E)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:[] for i in range(numCourses)}
        for i, v in prerequisites:
            d[i].append(v)

        visitSet = set()
        def dfs(node):
            if node in visitSet: return False
            if not d[node]: return True

            visitSet.add(node)
            for i in d[node]:
                if not dfs(i): return False
            visitSet.remove(node)
            d[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True

s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))

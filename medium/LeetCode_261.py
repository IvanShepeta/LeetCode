"""
------------------------------------------------------------
🧠 Problem: 261. Graph Valid Tree
🔗 Link: https://leetcode.com/problems/graph-valid-tree/
------------------------------------------------------------
📜 Description:
Given n nodes labeled from 0 to n-1 and a list of undirected edges,
check if these edges form a valid tree.

A valid tree satisfies two conditions:
1️⃣ It is connected: every node is reachable from any other node.
2️⃣ It contains no cycles: no node can be reached by two different paths.

💡 Example:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: True
Explanation: The graph is connected and has no cycles.

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: False
Explanation: The graph has a cycle: 1-2-3-1

🧩 Approach (Union-Find / DFS):
- Union-Find: Track connected components to detect cycles.
- DFS/BFS: Ensure all nodes are visited (connected) and no cycles exist.

⏱️ Time Complexity:  O(n + e)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)


s = Solution()
print(s.validTree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]))

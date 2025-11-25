"""
------------------------------------------------------------
🧠 Problem: 323. Number of Connected Components in an Undirected Graph
🔗 Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
------------------------------------------------------------
📜 Description:
You are given n nodes labeled from 0 to n-1 and a list of undirected edges.
Return the number of connected components in the graph.

💡 Example:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation: There are two connected components:
1. 0-1-2
2. 3-4

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
Explanation: All nodes are connected, so there is only one component.

🧩 Approach:
- Use Union-Find (Disjoint Set) to merge connected nodes and count components.
- Or DFS/BFS: iterate over all unvisited nodes, mark reachable nodes, increment component count.

⏱️ Time Complexity:  O(n + e)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components
        # par = [i for i in range(n)]
        # rank = [1] * n
        #
        # def find(n1):
        #     res = n1
        #
        #     while res != par[res]:
        #         par[res] = par[par[res]]
        #         res = par[res]
        #     return res
        #
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
        #     if p1 == p2:
        #         return 0
        #     if rank[p2] > rank[p1]:
        #         par[p1] = p2
        #         rank[p2] += rank[p1]
        #     else:
        #         par[p2] = p1
        #         rank[p1] += rank[p2]
        #     return 1
        # res = n
        # for n1, n2 in edges:
        #     res -= union(n1, n2)
        # return res


s = Solution()
print(s.countComponents(n=3, edges=[[0,1], [0,2]]))
print(s.countComponents(n=6, edges=[[0,1], [1,2], [2,3], [4,5]]))

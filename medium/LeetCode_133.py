"""
------------------------------------------------------------
🧠 Problem: 133. Clone Graph
🔗 Link: https://leetcode.com/problems/clone-graph/
------------------------------------------------------------
📜 Description:
Given a reference of a node in a connected undirected graph,
return a deep copy (clone) of the graph. Each node contains
a value and a list of neighbors.

💡 Example:
Input: adjacencyList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

🧩 Approach (DFS / BFS):
We can clone the graph using a recursive DFS (or iterative BFS)
keeping track of already cloned nodes in a dictionary.

Steps:
1. Use a dictionary `visited` to map original nodes → cloned nodes.
2. Recursively clone each neighbor.
3. Return the cloned node.

⏱️ Time Complexity:  O(V + E)  (V = #nodes, E = #edges)
💾 Space Complexity: O(V)      (for visited map + recursion stack)
------------------------------------------------------------
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

s = Solution()
clone = s.cloneGraph(node1)

print("Original:", node1.val, "Neighbors:", [n.val for n in node1.neighbors])
print("Clone:", clone.val, "Neighbors:", [n.val for n in clone.neighbors])

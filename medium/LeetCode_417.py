"""
------------------------------------------------------------
🧠 Problem: 417. Pacific Atlantic Water Flow
🔗 Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
------------------------------------------------------------
📜 Description:
Given an m x n matrix of heights, find all cells where water
can flow to both the Pacific and Atlantic oceans. Water can
flow from a cell to neighboring cells (up, down, left, right)
if the neighbor's height is less than or equal to the current cell.

💡 Example:
Input:
    heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ]
Output:
    [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

🧩 Approach (DFS + Sets):
1. Perform DFS starting from Pacific borders (top row + left column)
   and mark all reachable cells in `pac` set.
2. Perform DFS starting from Atlantic borders (bottom row + right column)
   and mark all reachable cells in `atl` set.
3. For each cell, if it exists in both sets → water can flow to both oceans.

⏱️ Time Complexity: O(M*N)
💾 Space Complexity: O(M*N) for sets and recursion stack
------------------------------------------------------------
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r+1,c,visit, heights[r][c])
            dfs(r-1,c,visit, heights[r][c])
            dfs(r,c+1,visit, heights[r][c])
            dfs(r,c-1,visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])
        return res

s = Solution()
print(s.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(s.pacificAtlantic(heights = [[1,1],[1,1],[1,1]]))
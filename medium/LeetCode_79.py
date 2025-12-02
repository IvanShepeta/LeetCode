"""
------------------------------------------------------------
🧠 Problem: 79. Word Search
🔗 Link: https://leetcode.com/problems/word-search/
------------------------------------------------------------
📜 Description:
Given an m x n grid of characters board and a string word, return
true if the word exists in the grid.

The word can be constructed from sequentially adjacent cells
(horizontally or vertically), and the same cell *must not* be
used more than once.

💡 Example:
Input:
board = [
 ["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]
]
word = "ABCCED"
Output: True

Input:
board = [["a","b"],["c","d"]]
word = "abcd"
Output: False

🧩 Approach (DFS + Backtracking):
1. For every position in grid, start DFS search.
2. If current cell matches current character:
   - Add it to visited set
   - Recursively search neighbors (up, down, left, right)
   - Backtrack (remove from set)
3. If we match all characters → return True.

⏱️ Time Complexity:  O(m * n * 4^L)   # L = length of word
💾 Space Complexity: O(L)
------------------------------------------------------------
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r<0 or r>=ROWS or c<0 or c>=COLS or word[i] != board[r][c] or (r, c) in path:
                return False

            path.add((r, c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))


            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False



s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
        
"""
------------------------------------------------------------
🧠 Problem: 73. Set Matrix Zeroes
🔗 Link: https://leetcode.com/problems/set-matrix-zeroes/
------------------------------------------------------------
📜 Description:
Given an m x n matrix, if an element is 0, set its entire row
and column to 0. Do it *in-place*.

💡 Example:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [0,0,0],
  [0,0,0],
  [1,0,1]
]

🧩 Approach (O(1) extra space):
We cannot create a second matrix.
To avoid losing information, we use the *first row* and *first column*
as markers:

1. First pass:
   - If matrix[i][j] == 0 :
        mark row i → matrix[i][0] = 0
        mark col j → matrix[0][j] = 0
   - Track separately whether the first column needs to be zeroed.

2. Second pass (from bottom-right):
   - Use markers to set cells to zero.

⏱️ Time Complexity:  O(m * n)
💾 Space Complexity: O(1)   (in-place, uses markers)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        cols0 = False
        for r in range(rows):
            if matrix[r][0] == 0:
                cols0 = True
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, 0, -1):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

            if cols0:
                matrix[r][0] = 0

        return matrix



s = Solution()
print(s.setZeroes([[1,1,1],
                   [1,0,1],
                   [1,1,1]]))

print(s.setZeroes([[0,1,2,0],
                   [3,4,5,2],
                   [1,3,1,5]]))

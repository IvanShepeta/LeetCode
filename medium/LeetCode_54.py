"""
------------------------------------------------------------
🧠 Problem: 54. Spiral Matrix
🔗 Link: https://leetcode.com/problems/spiral-matrix/
------------------------------------------------------------
📜 Description:
Given an m x n matrix, return all elements of the matrix in
spiral order.

💡 Example:
Input: matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
Output: [1,2,3,6,9,8,7,4,5]

🧩 Approach (Layer by Layer Simulation):
1. Maintain boundaries: top, bottom, left, right.
2. Traverse the matrix in the order:
   - Left → Right (top row)
   - Top → Bottom (right column)
   - Right → Left (bottom row)
   - Bottom → Top (left column)
3. Shrink boundaries after each side is processed.
4. Repeat until all elements are collected.
5. Add a break condition to avoid over-traversal in single-row/column cases.

⏱️ Time Complexity:  O(m * n)
💾 Space Complexity: O(1) extra space (excluding output list)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while top < bottom and left < right:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right -1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # get every i in the left col
            for i in range(bottom-1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


s = Solution()
print(s.spiralOrder(matrix = [[1,2,3],
                              [4,5,6],
                              [7,8,9]]))  # Output: [1,2,3,6,9,8,7,4,5]

print(s.spiralOrder(matrix = [[1,2,3,4],
                              [5,6,7,8],
                              [9,10,11,12]])) # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

print(s.spiralOrder(matrix = [[1,2],
                              [3,4]])) # Output: [1,2,4,3]
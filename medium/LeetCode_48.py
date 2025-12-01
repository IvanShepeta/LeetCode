"""
------------------------------------------------------------
🧠 Problem: 48. Rotate Image
🔗 Link: https://leetcode.com/problems/rotate-image/
------------------------------------------------------------
📜 Description:
You are given an n x n 2D matrix representing an image. Rotate
the image by 90 degrees (clockwise) in-place.

💡 Example:
Input: matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
Output: [
 [7,4,1],
 [8,5,2],
 [9,6,3]
]

🧩 Approach (Transpose + Reverse):
1. Transpose the matrix (swap matrix[i][j] with matrix[j][i]).
2. Reverse each row to achieve 90° clockwise rotation.
3. This is done in-place without using extra space.

⏱️ Time Complexity:  O(n^2)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix

s = Solution()

print(s.rotate([[1,2,3],
                [4,5,6],
                [7,8,9]])) # Output: [[7,4,1],[8,5,2],[9,6,3]]

print(s.rotate([[5,1,9,11],
                [2,4,8,10],
                [13,3,6,7],
                [15,14,12,16]])) # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
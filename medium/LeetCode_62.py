"""
------------------------------------------------------------
🧠 Problem: 62. Unique Paths
🔗 Link: https://leetcode.com/problems/unique-paths/
------------------------------------------------------------
📜 Description:
A robot is located at the top-left corner of an m x n grid.
The robot can only move:
  ➤ Right
  ➤ Down

Find the number of unique paths to reach the bottom-right corner.

💡 Example:
Input: m = 3, n = 7
Output: 28

🧩 Approach (Dynamic Programming):
We fill a DP table from bottom-right to top-left.
Each cell dp[i][j] represents the number of ways to reach the finish.
Formula:
    dp[i][j] = dp[i+1][j] + dp[i][j+1]

Base case:
    dp[m-1][n-1] = 1   (finish)

⏱️ Time Complexity:  O(m * n)
💾 Space Complexity: O(m * n)
------------------------------------------------------------
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0 for i in range(n+1)] for i in range(m + 1)]
        # dp[m-1][n-1] = 1
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i == m-1 and j == n-1:
        #             continue
        #         dp[i][j] = dp[i][j+1] + dp[i+1][j]
        # return dp[0][0]

        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


s =Solution()
print(s.uniquePaths( m = 3, n = 7))
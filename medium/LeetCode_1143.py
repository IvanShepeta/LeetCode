"""
------------------------------------------------------------
🧠 Problem: 1143. Longest Common Subsequence
🔗 Link: https://leetcode.com/problems/longest-common-subsequence/
------------------------------------------------------------
📜 Description:
Given two strings text1 and text2, return the length of their
longest common subsequence (LCS).

A subsequence appears in the same order but not necessarily
contiguously.

💡 Example:
Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The LCS is "ace".

⏱️ Time Complexity:  O(n * m)
💾 Space Complexity: O(n * m)
------------------------------------------------------------
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0 for j in range(len(text2) + 1)]for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
# DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

s = Solution()
print(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
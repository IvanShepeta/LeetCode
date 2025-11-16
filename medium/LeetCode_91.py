"""
------------------------------------------------------------
🔢 Problem: 91. Decode Ways
🔗 Link: https://leetcode.com/problems/decode-ways/
------------------------------------------------------------
📜 Description:
Given a string `s` containing only digits, return the number of ways
to decode it according to the following mapping:

    '1' → 'A'
    '2' → 'B'
    ...
    '26' → 'Z'

Example:
Input:  "226"
Output: 3
( "2 2 6" → "BBF", "22 6" → "VF", "2 26" → "BZ" )

🧩 Key Idea:
Dynamic Programming.

Let `dp[i]` = number of ways to decode substring `s[:i]`.

Rules:
1️⃣ If single digit `s[i-1]` is valid (1–9), then:
        dp[i] += dp[i - 1]

2️⃣ If two digits `s[i-2:i]` are valid (10–26), then:
        dp[i] += dp[i - 2]

We build dp bottom-up.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1) (optimized)
------------------------------------------------------------
"""

class Solution:
    def numDecodings(self, s: str) -> int:


        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)


s = Solution()
print(s.numDecodings("12"))

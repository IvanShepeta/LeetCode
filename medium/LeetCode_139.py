"""
------------------------------------------------------------
🧠 Problem: 139. Word Break
🔗 Link: https://leetcode.com/problems/word-break/
------------------------------------------------------------
📜 Description:
Given a string s and a list of words wordDict, determine if s
can be segmented into a space-separated sequence of dictionary words.

💡 Example:
Input:  s = "leetcode", wordDict = ["leet","code"]
Output: True
Explanation: "leetcode" = "leet" + "code"

🧩 Approach (Dynamic Programming):
We use a boolean DP array:

- dp[i] = True if the suffix s[i:] can be segmented into words in wordDict

Algorithm:

1️⃣ Initialize dp:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True   # empty string is segmentable

2️⃣ Iterate i from len(s)-1 down to 0:
    - For each word w in wordDict:
        - Check if s[i:i+len(w)] == w and i+len(w) <= len(s)
        - If so, set dp[i] = dp[i + len(w)]
        - If dp[i] is True, break (early stop)

3️⃣ Return dp[0] → True if entire string can be segmented

⏱️ Time Complexity:  O(n * m * k)
    - n = len(s), m = number of words, k = average length of word
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
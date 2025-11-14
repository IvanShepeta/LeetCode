"""
------------------------------------------------------------
🧠 Problem: 322. Coin Change
🔗 Link: https://leetcode.com/problems/coin-change/
------------------------------------------------------------
📜 Description:
Given an array of coin denominations and a target amount,
return the minimum number of coins needed to make that amount.
If it's not possible, return -1.

💡 Example:
Input:  coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

🧩 Approach:
This is a classic Dynamic Programming problem.

Let dp[x] = minimum number of coins needed to make amount x.

Initialize dp with:
- dp[0] = 0  (0 coins needed to make 0)
- dp[i] = infinity for all i > 0

For each amount from 1 to target:
    For each coin:
        If (amount - coin) >= 0:
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

At the end:
- If dp[amount] is still infinity → return -1
- Otherwise → return dp[amount]

⏱️ Time Complexity: O(amount * number_of_coins)
💾 Space Complexity: O(amount)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1



s = Solution()
print(s.coinChange(coins = [2], amount = 3))
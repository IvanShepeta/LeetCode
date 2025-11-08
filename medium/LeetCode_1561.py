"""
------------------------------------------------------------
🧠 Problem: 1561. Maximum Number of Coins You Can Get
🔗 Link: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
------------------------------------------------------------
📜 Description:
You and two friends (Alice and Bob) take turns picking piles of coins:
- Alice picks the pile with the most coins.
- You pick the next largest pile.
- Bob takes the smallest pile.

Repeat until no piles remain.

💡 Example:
Input:  piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
Output: 18

🧩 Approach:
1. Sort piles in descending order.
2. In each round of 3 piles → skip Alice’s max and Bob’s min.
3. Take the second largest (index pattern 1, 3, 5, ...).

⏱️ Time Complexity:  O(n log n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        a = sorted(piles, reverse=True)
        r = 0
        for i in range(len(piles) // 3):
            r += a[(i*2)+1]
        return r

s = Solution()
result = s.maxCoins([9,8,7,6,5,1,2,3,4])
print(result)
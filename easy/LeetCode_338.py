"""
------------------------------------------------------------
🧠 Problem: 338. Counting Bits
🔗 Link: https://leetcode.com/problems/counting-bits/
------------------------------------------------------------
📜 Description:
Given an integer n, return an array `ans` of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the
binary representation of i.

💡 Example:
Input:  n = 5
Output: [0, 1, 1, 2, 1, 2]
Explanation:
0 -> 0
1 -> 1
2 -> 10
3 -> 11
4 -> 100
5 -> 101

⏱️ Time Complexity:
- Naive: O(n log n)
- DP: O(n)

💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        db = [0] * (n + 1)
        offset = 1

        for i in range(1 , n + 1):
            if offset * 2 == i:
                offset = i
            db[i] = 1 + db[i - offset]
        return db


s = Solution()
print(s.countBits(n = 2))

"""
------------------------------------------------------------
🧠 Problem: 198. House Robber
🔗 Link: https://leetcode.com/problems/house-robber/
------------------------------------------------------------
📜 Description:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, represented by nums.
You cannot rob two adjacent houses. Find the maximum amount of money you can rob without alerting the police.

💡 Example:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1) = 2 + 9 + 1 = 12

🧩 Approach (Dynamic Programming):
- For each house, you have two options:
    1️⃣ Skip this house → take the maximum sum until the previous house (dp[i-1])
    2️⃣ Rob this house → add its value to the maximum sum until the house before the previous one (dp[i-2] + nums[i])
- Formula: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
- Optimize to O(1) space by keeping only two variables: prev1 and prev2

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + n)
        return rob2
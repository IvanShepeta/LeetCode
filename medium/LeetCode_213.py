"""
------------------------------------------------------------
🏠 Problem: 213. House Robber II
🔗 Link: https://leetcode.com/problems/house-robber-ii/
------------------------------------------------------------
📜 Description:
You are given an array `nums`, where each element represents the amount of money
in a house arranged **in a circle**. Adjacent houses cannot both be robbed.

Return the maximum money you can rob.

💡 Key Insight:
You **cannot** rob both the first and last house since they are adjacent.

Therefore:
- Case 1 → Rob houses from index 1 to end    (exclude first house)
- Case 2 → Rob houses from index 0 to end-1  (exclude last house)
- Take the maximum of the two cases.

This reduces the problem to the classic *House Robber I*.

🧠 Helper logic (House Robber I):
Use DP with two variables:
- `rob1`: max robbed up to previous house
- `rob2`: max robbed up to current house

Transition:
    rob1, rob2 = rob2, max(rob2, rob1 + n)

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + n)
        return rob2

s = Solution()
print(s.rob(nums = [2,3,2]))

"""
------------------------------------------------------------
🧠 Problem: 55. Jump Game
🔗 Link: https://leetcode.com/problems/jump-game/
------------------------------------------------------------
📜 Description:
Given an array of non-negative integers nums, where each element
represents the maximum jump length from that position, determine
if you can reach the last index starting from the first index.

💡 Example:
Input: nums = [2,3,1,1,4]
Output: True

Input: nums = [3,2,1,0,4]
Output: False

🧩 Approach (Greedy):
We keep track of the furthest position we can reach.
At each index i:
    - If i > furthest, we can't move further → return False
    - Update furthest = max(furthest, i + nums[i])
    - If furthest >= last index → return True

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finish = len(nums) - 1
        start = 0
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= finish:
                finish = i
        return True if finish == 0 else False

        # for i, v in enumerate(nums):
        #     if i > start:
        #         return False
        #     start = max(start, i + v)
        #     if start >= finish:
        #         return True
        #
        # return False


s = Solution()

assert s.canJump([2,3,1,1,4])
assert s.canJump([2,0])
assert s.canJump([3,2,1,0,4]) == False
assert s.canJump([0,1]) == False
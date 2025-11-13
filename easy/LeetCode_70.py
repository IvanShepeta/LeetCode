"""
------------------------------------------------------------
🧠 Problem: 70. Climbing Stairs
🔗 Link: https://leetcode.com/problems/climbing-stairs/
------------------------------------------------------------
📜 Description:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

💡 Example:
Input:  n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1

🧩 Approach:
This is essentially a Fibonacci sequence problem:
- ways(n) = ways(n-1) + ways(n-2)
- Use two variables to store previous two results to avoid extra space.

⏱️ Time Complexity: O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n):
            one, two = one + two, one
        return two

s = Solution()

print(s.climbStairs(3))

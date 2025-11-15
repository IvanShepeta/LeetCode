"""
------------------------------------------------------------
🧠 Problem: 39. Combination Sum
🔗 Link: https://leetcode.com/problems/combination-sum/
------------------------------------------------------------
📜 Description:
Given an array of distinct integers `candidates` and a target integer `target`,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may use the same number from candidates unlimited times.

💡 Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2+2+3=7 and 7=7

🧩 Approach (Backtracking / DFS):
- Use recursion to explore all possible combinations.
- At each step, either include the current number (and continue) or skip it.
- Stop recursion if sum exceeds target.
- Collect all combinations that exactly sum to target.

⏱️ Time Complexity:  O(2^t) where t is target / min(candidates)
💾 Space Complexity: O(t) for recursion stack
------------------------------------------------------------
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total == 0:
                res.append(path.copy())
                return
            if total < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                backtrack(i, path, total - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res
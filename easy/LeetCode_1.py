"""
------------------------------------------------------------
💡 Problem: 1. Two Sum
🔗 Link: https://leetcode.com/problems/two-sum/
------------------------------------------------------------
📜 Description:
Given an array of integers `nums` and an integer `target`,
return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

------------------------------------------------------------
🧩 Approach:
- Use a HashMap (dictionary) to store each number’s value and its index.
- For each element, check if (target - current_value) already exists in the map.
- If yes → return the stored index and current index.
- If no → store current_value and its index in the map.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in d:
                return [d[c], i]

            d[num] = i
        return None


s = Solution()
result = s.twoSum(nums = [3,2,4], target = 6)
print(result)




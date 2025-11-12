"""
------------------------------------------------------------
🧠 Problem: 268. Missing Number
🔗 Link: https://leetcode.com/problems/missing-number/
------------------------------------------------------------
📜 Description:
Given an array `nums` containing n distinct numbers taken from 0, 1, 2, ..., n,
return the one number that is missing from the array.

💡 Example:
Input:  nums = [3,0,1]
Output: 2

Input:  nums = [0,1]
Output: 2

⏱️ Time Complexity: O(n)
💾 Space Complexity: O(1) for sum/XOR, O(n) for set approach
------------------------------------------------------------
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        l = len(nums)
        res = (l*(l+1)) // 2 - total
        return res
        # res = len(nums)
        # for i in range(len(nums)):
        #     res += (i - nums[i])
        # return res

s = Solution()
print(s.missingNumber(nums = [3,0,1]))
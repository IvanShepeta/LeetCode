"""
------------------------------------------------------------
🧠 Problem: 53. Maximum Subarray
🔗 Link: https://leetcode.com/problems/maximum-subarray/
------------------------------------------------------------
📜 Description:
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

💡 Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

🧩 Approach:
Use Kadane’s Algorithm.
Iterate through the array while tracking the current subarray sum.
If the running sum becomes negative, reset it to the current element.
Keep updating the global maximum sum during iteration.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
----
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0
        current_sum = 0
        for i in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += i
            result = max(result, current_sum)
        return result


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

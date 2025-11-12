"""
------------------------------------------------------------
🧠 Problem: 15. 3Sum
🔗 Link: https://leetcode.com/problems/3sum/
------------------------------------------------------------
📜 Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

💡 Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

🧩 Approach:
1. Sort the array to handle duplicates easily.
2. Fix one number (nums[i]), then use two pointers (left, right)
   to find two other numbers whose sum equals -nums[i].
3. Skip duplicates to avoid repeating the same triplet.

⏱️ Time Complexity:  O(n²)
💾 Space Complexity: O(1) (excluding the result list)
------------------------------------------------------------
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                three = num + nums[l] + nums[r]
                if three > 0:
                    r -= 1
                elif three < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

s = Solution()
print(s.threeSum([0,0,0,0]))
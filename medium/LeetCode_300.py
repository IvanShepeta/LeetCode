"""
------------------------------------------------------------
🧠 Problem: 300. Longest Increasing Subsequence
🔗 Link: https://leetcode.com/problems/longest-increasing-subsequence/
------------------------------------------------------------
📜 Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

💡 Example:
Input:  nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101].

🧩 Approach:
Dynamic Programming (classic solution):

1️⃣ DP Approach (O(n^2)):
- Let dp[i] = length of the longest increasing subsequence ending at index i.
- For each i, check all j < i:
    - if nums[j] < nums[i], we can extend the subsequence ending at j.
    - dp[i] = max(dp[i], dp[j] + 1)
- Answer = max(dp)

2️⃣ Optimized Approach (O(n log n)):
- Use a list "sub" to maintain the current increasing subsequence.
- For each number, use binary search to find the position to replace or append.
- Length of "sub" at the end = length of LIS.

⏱️ Time Complexity:
- DP: O(n^2)
- Optimized: O(n log n)
💾 Space Complexity:
- DP: O(n)
- Optimized: O(n)
------------------------------------------------------------
"""
from typing import List

# Approach 1: DP O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)


# Approach 2: Optimized O(n log n)
from bisect import bisect_left

class SolutionOptimized:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i < len(sub):
                sub[i] = num
            else:
                sub.append(num)
        return len(sub)

s = Solution()
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))

"""
------------------------------------------------------------
🧠 Problem: 128. Longest Consecutive Sequence
🔗 Link: https://leetcode.com/problems/longest-consecutive-sequence/
------------------------------------------------------------
📜 Description:
Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence.

⚠️ You must write an algorithm that runs in O(n) time.

💡 Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

🧩 Approach (Hash Set):
- Put all numbers into a hash set → O(1) average lookup time.
- For each number, check if it is the **start** of a sequence:
    A number is a start if (num - 1) is NOT in the set.
- If it's a start, count how long the sequence continues (num+1, num+2, ...).
- Track the longest sequence length.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                l = 1
                while n + l in nums:
                    l += 1
                res = max(res, l)
        return res

s = Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))

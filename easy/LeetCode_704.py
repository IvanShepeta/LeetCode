"""
------------------------------------------------------------
🧠 Problem: 704. Binary Search
🔗 Link: https://leetcode.com/problems/binary-search/
------------------------------------------------------------
📜 Description:
Given a sorted array of integers `nums` and an integer `target`,
return the index of `target` if it exists, otherwise return -1.

💡 Example:
Input:  nums = [-1,0,3,5,9,12], target = 9
Output: 4

🧩 Approach:
Use binary search (divide and conquer):
- Compare middle element with target.
- Narrow search range accordingly until found or range is empty.

⏱️ Time Complexity:  O(log n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


s = Solution()
result = s.search([-1,0,3,5,9,12], 9)
print(result)
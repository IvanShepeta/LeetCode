"""
------------------------------------------------------------
🧠 Problem: 33. Search in Rotated Sorted Array
🔗 Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
------------------------------------------------------------
📜 Description:
You are given a rotated sorted array `nums` and a target value `target`.
Return the index of `target` if it exists, otherwise return -1.

💡 Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

🧩 Approach:
Use modified binary search:
- The array is rotated, but one of the halves (left or right) is always sorted.
- Determine which half is sorted and decide where to continue the search.

⏱️ Time Complexity:  O(log n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1

            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))

"""
------------------------------------------------------------
🧠 Problem: 153. Find Minimum in Rotated Sorted Array
🔗 Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
------------------------------------------------------------
📜 Description:
Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. For example, the array [0,1,2,4,5,6,7]
might become [4,5,6,7,0,1,2].

Find the minimum element in the rotated sorted array.
You must do this in O(log n) time.

💡 Example:
Input: nums = [3,4,5,1,2]
Output: 1

🧩 Approach:
Use Binary Search:
- If nums[mid] > nums[right], the minimum is in the right half.
- Otherwise, it's in the left half (including mid).
Continue until left == right, which will be the index of the minimum.

⏱️ Time Complexity:  O(log n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List
import numpy as np


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # result = np.min(nums)
        # return int(result)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


s = Solution()
print(s.findMin([2, 3, 4, 5, 1]))

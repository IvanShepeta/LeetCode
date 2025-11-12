"""
------------------------------------------------------------
🧠 Problem: 11. Container With Most Water
🔗 Link: https://leetcode.com/problems/container-with-most-water/
------------------------------------------------------------
📜 Description:
Given n non-negative integers `height[i]` where each represents a vertical line
on the x-axis, find two lines that together with the x-axis form a container,
such that the container holds the **most water**.

💡 Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

🧩 Approach:
Use the **two-pointer technique**:
- Start with left pointer at 0 and right pointer at n - 1
- Compute area = (right - left) * min(height[left], height[right])
- Move the pointer that points to the shorter line (since it limits the height)
- Keep track of the maximum area

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

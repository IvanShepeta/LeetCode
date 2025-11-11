"""
------------------------------------------------------------
🧠 Problem: 152. Maximum Product Subarray
🔗 Link: https://leetcode.com/problems/maximum-product-subarray/
------------------------------------------------------------
📜 Description:
Given an integer array nums, find the contiguous subarray
within the array (containing at least one number)
which has the largest product, and return that product.

💡 Example:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has the largest product = 6.

🧩 Approach:
We need to track both the maximum and minimum products
at each position because a negative number can turn
a small (negative) product into a large positive one.

At each step:
- temp_max = max(nums[i], nums[i]*max_prod, nums[i]*min_prod)
- temp_min = min(nums[i], nums[i]*max_prod, nums[i]*min_prod)
- Update global result with temp_max.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low = 1
        high = 1
        res = max(nums)
        for i in nums:
            if i == 0:
                low, high = 1, 1
                continue
            temp = high*i
            high = max(i*high, i*low, i)
            low = min(temp, i*low, i)
            res = max(res, high)
        return res


s = Solution()
print(s.maxProduct(nums = [2,3,-2,4]))
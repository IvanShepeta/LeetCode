"""
------------------------------------------------------------
🧠 Problem: 238. Product of Array Except Self
🔗 Link: https://leetcode.com/problems/product-of-array-except-self/
------------------------------------------------------------
📜 Description:
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

💡 Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

🧩 Approach:
- Use two passes: first pass computes prefix product, second pass computes suffix product.
- Do not use division.
- Achieves O(n) time and O(1) extra space (excluding output array).

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1) extra (output array not counted)
------------------------------------------------------------
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

s = Solution()
result = s.productExceptSelf(nums = [1,2,3,4])
print(result)
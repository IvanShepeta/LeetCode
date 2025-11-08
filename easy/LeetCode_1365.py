"""
------------------------------------------------------------
🧠 Problem: 1365. How Many Numbers Are Smaller Than the Current Number
🔗 Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
------------------------------------------------------------
📜 Description:
For each number in `nums`, count how many numbers are smaller than it.

💡 Example:
Input:  nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

🧩 Approach:
- Sort a copy of nums.
- Map each unique number → its first index (count of smaller elements).
- Replace each number with its mapped value.

⏱️ Time Complexity:  O(n log n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # r = []
        # count = 0
        # for num in nums:
        #     for other in nums:
        #         if num > other:
        #             count += 1
        #     r.append(count)
        #     count = 0
        # return r
        r = sorted(nums)
        di = {}
        for i, j in enumerate(r):
            if j not in di:
                di[j] = i
        res = []
        for i in nums:
            res.append(di[i])
        return res

s = Solution()
nums = [8,1,2,2,3]
result = s.smallerNumbersThanCurrent(nums)
print(result)
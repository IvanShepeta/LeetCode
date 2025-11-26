"""
------------------------------------------------------------
🧠 Problem: 435. Non-overlapping Intervals
🔗 Link: https://leetcode.com/problems/non-overlapping-intervals/
------------------------------------------------------------
📜 Description:
Given a collection of intervals, find the minimum number of
intervals you need to remove to make the rest of the intervals
non-overlapping.

💡 Example:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: Remove [1,3] and the rest are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: Remove two intervals to avoid overlap.

🧩 Approach (Greedy / Sorting):
1. Sort intervals by end time.
2. Keep track of the end of the last added interval.
3. For each interval:
   - If it starts after or at the end of the last interval → keep it.
   - Else → remove it (count as overlap).
4. Return the number of removed intervals.

⏱️ Time Complexity:  O(n log n)  # sorting
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        end = intervals[0][1]

        for i in intervals[1:]:
            if i[0] >= end:
                end = i[1]
            else:
                res +=1
                end = min(end,i[1])
        return res



s = Solution()
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
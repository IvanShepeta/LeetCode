"""
------------------------------------------------------------
🧠 Problem: 56. Merge Intervals
🔗 Link: https://leetcode.com/problems/merge-intervals/
------------------------------------------------------------
📜 Description:
Given a collection of intervals, merge all overlapping intervals
and return an array of the non-overlapping intervals sorted
by start times.

💡 Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

🧩 Approach (Greedy / Sorting):
1. Sort intervals by start time.
2. Initialize merged list with the first interval.
3. Iterate over intervals:
   - If current interval overlaps with last merged → merge them.
   - Else → append current interval to merged list.

⏱️ Time Complexity:  O(n log n)  # sorting
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]
        for start, end in intervals[1:]:
            last = res[-1][1]
            if last >= start:
                res[-1][1] = max(last, end)
            else:
                res.append([start,end])

        return res


s = Solution()
print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(s.merge(intervals = [[4,7],[1,4]]))
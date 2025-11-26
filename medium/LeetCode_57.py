"""
------------------------------------------------------------
🧠 Problem: 57. Insert Interval
🔗 Link: https://leetcode.com/problems/insert-interval/
------------------------------------------------------------
📜 Description:
Given a list of non-overlapping intervals sorted by start times,
and a new interval, insert the new interval into the list such
that the intervals remain sorted and non-overlapping. Merge if
necessary.

💡 Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

🧩 Approach (Greedy / Merge Intervals):
1. Add all intervals that end before the new interval starts.
2. Merge all intervals that overlap with the new interval.
3. Add all remaining intervals.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        left, right = 0, len(intervals)
        while left < right and intervals[left][1] < newInterval[0]:
            res.append(intervals[left])
            left += 1

        while left < right and intervals[left][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[left][1])
            left += 1
        res.append(newInterval)

        while left < right:
            res.append(intervals[left])
            left += 1

        return res

        # for i in range(len(intervals)):
        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        # res.append(newInterval)
        # return res

s = Solution()
print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
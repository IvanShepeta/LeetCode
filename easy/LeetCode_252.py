"""
------------------------------------------------------------
🧠 Problem: 252. Meeting Rooms
🔗 Link: https://leetcode.com/problems/meeting-rooms/
------------------------------------------------------------
📜 Description:
Given an array of meeting time intervals where each interval
is represented as [start, end], determine if a person can attend
all meetings (i.e., no intervals overlap).

💡 Example:
Input:  [[0,30],[5,10],[15,20]]
Output: False  (0–30 overlaps with 5–10)

Input:  [[7,10],[2,4]]
Output: True

🧩 Approach (Sort + Check Overlaps):
1. Sort intervals by start time.
2. For each interval, check whether its start time
   overlaps the previous interval’s end time.
3. If any overlap exists → return False.
4. Otherwise → return True.

⏱️ Time Complexity:  O(n log n)  (sorting)
💾 Space Complexity: O(1)        (in-place)
------------------------------------------------------------
"""
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda k: k.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True


s = Solution()
print(s.canAttendMeetings(intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]))
print(s.canAttendMeetings(intervals = [Interval(5,8),Interval(9,15)]))

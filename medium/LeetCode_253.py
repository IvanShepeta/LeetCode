"""
------------------------------------------------------------
🧠 Problem: 253. Meeting Rooms II
🔗 Link: https://leetcode.com/problems/meeting-rooms-ii/
------------------------------------------------------------
📜 Description:
Given meeting intervals, return the **minimum number of rooms**
needed so that all meetings can happen without conflicts.

💡 Example:
Input:  [[0,30],[5,10],[15,20]]
Output: 2

Explanation:
- Meeting1: [0,30]
- Meeting2:     [5,10]
→ Meeting2 overlaps → need 2 rooms

🧩 Approach (Min-Heap):
1. Sort intervals by start time.
2. Use a **min-heap** to store end times of current meetings.
3. For each interval:
       - If earliest-ending meeting finished → reuse room (heap pop)
       - Else → need new room
       - Push current meeting end time
4. Heap size = number of active rooms.

⏱️ Time Complexity:  O(n log n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


s = Solution()
print(s.minMeetingRooms(intervals = [Interval(0,40),Interval(5,10),Interval(15,20)]))
print(s.minMeetingRooms(intervals = [Interval(4,9)]))
print(s.minMeetingRooms(intervals = [Interval(1,5),Interval(2,6),Interval(3,7),Interval(4,8),Interval(5,9)]))
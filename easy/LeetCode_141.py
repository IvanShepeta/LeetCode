"""
------------------------------------------------------------
🧠 Problem: 141. Linked List Cycle
🔗 Link: https://leetcode.com/problems/linked-list-cycle/
------------------------------------------------------------
📜 Description:
Given the head of a singly linked list, determine if the list
contains a cycle. A cycle exists if a node’s `next` pointer
eventually points to a previously visited node.

💡 Example:
Input: head = [3,2,0,-4], pos = 1
Output: True

Input: head = [1,2], pos = 0
Output: True

Input: head = [1], pos = -1
Output: False

🧩 Approach (Floyd's Tortoise and Hare):
Use two pointers:
  - slow moves 1 step at a time
  - fast moves 2 steps at a time

If there is no cycle → fast reaches the end.
If there *is* a cycle → fast and slow eventually meet.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_list_with_cycle(values, pos):
    """
    pos = cycle node
    pos = -1 → There is no cycle
    """
    
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    if pos != -1:
        nodes[-1].next = nodes[pos]  # створюємо цикл

    return nodes[0]

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

s = Solution()
res = s.hasCycle(build_list_with_cycle([3,2,0,-4], pos= 1))
print(res)
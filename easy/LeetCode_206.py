"""
------------------------------------------------------------
🧠 Problem: 206. Reverse Linked List
🔗 Link: https://leetcode.com/problems/reverse-linked-list/
------------------------------------------------------------
📜 Description:
Given the head of a singly linked list, reverse the list and
return the reversed list.

💡 Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

🧩 Approach (Iterative / In-place):
1. Initialize two pointers: prev = None, curr = head.
2. Iterate through the list:
   - Save next node: next_temp = curr.next
   - Reverse pointer: curr.next = prev
   - Move prev and curr forward: prev = curr, curr = next_temp
3. Return prev (new head of reversed list)

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to convert Python list -> ListNode
def list_to_linked(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

#Function to convert ListNode -> Python list
def linked_to_list(head: Optional[ListNode]):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head
        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # return prev
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

s = Solution()
res = s.reverseList(list_to_linked([1,2,3,4,5]))
print(linked_to_list(res))
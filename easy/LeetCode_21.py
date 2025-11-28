"""
------------------------------------------------------------
🧠 Problem: 21. Merge Two Sorted Lists
🔗 Link: https://leetcode.com/problems/merge-two-sorted-lists/
------------------------------------------------------------
📜 Description:
Given the heads of two sorted linked lists, merge them into a
single sorted linked list. Return the merged list.

💡 Example:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

🧩 Approach (Iterative / Two Pointers):
1. Create a dummy node to simplify handling the head.
2. Use two pointers, one for each list:
   - Compare current nodes of both lists
   - Attach the smaller node to the merged list
   - Move pointer forward in the list where node was taken
3. Attach any remaining nodes from either list
4. Return dummy.next as the head of merged list

⏱️ Time Complexity:  O(n + m)  # n, m = lengths of lists
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res

        while list1 and list1:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return res.next


def printList(node):
    while node:
        print(f"{node.val}" + (" -> " if node.next else ""), end="")
        node = node.next
    print()

if __name__ == "__main__":
    s = Solution()

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    result = s.mergeTwoLists(head1, head2)

    printList(result)
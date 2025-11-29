"""
------------------------------------------------------------
🧠 Problem: 19. Remove Nth Node From End of List
🔗 Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
------------------------------------------------------------
📜 Description:
Given the head of a linked list, remove the n-th node from the
end of the list and return the new head.

💡 Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

🧩 Approach (Two Pointers):
1. Use a dummy node before head to handle edge cases.
2. Move a fast pointer n steps ahead.
3. Move slow and fast pointers together until fast reaches the end.
4. Now slow is right before the node to delete → slow.next = slow.next.next

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(node):
    while node:
        print(f"{node.val}" + (" -> " if node.next else ""), end="")
        node = node.next
    print()

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)


    result = s.removeNthFromEnd(head1, n=2)

    printList(result)
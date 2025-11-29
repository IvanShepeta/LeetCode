"""
------------------------------------------------------------
🧠 Problem: 143. Reorder List
🔗 Link: https://leetcode.com/problems/reorder-list/
------------------------------------------------------------
📜 Description:
You are given the head of a singly linked list.
Reorder the list so that the nodes appear in the following order:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You must do this *in-place* without modifying node values — only links.

💡 Example:
Input:  head = [1,2,3,4]
Output: [1,4,2,3]

Input:  head = [1,2,3,4,5]
Output: [1,5,2,4,3]

🧩 Approach (Three Steps):
1. **Find the middle** using fast/slow pointers.
2. **Reverse the second half** of the list.
3. **Merge two halves**:
      - first:  L0 → L1 → L2 → ...
      - second: Ln → Ln-1 → ...

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
    def reorderList(self, head: Optional[ListNode]):
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle position
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        #reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge two halfs
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next ,second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        return head

if __name__ == "__main__":
    s = Solution()

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)

    result = s.reorderList(head1)

    printList(result)
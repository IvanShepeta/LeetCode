"""
------------------------------------------------------------
🧠 Problem: 23. Merge k Sorted Lists
🔗 Link: https://leetcode.com/problems/merge-k-sorted-lists/
------------------------------------------------------------
📜 Description:
Given an array of k linked lists, each sorted in ascending order,
merge all the lists into one sorted linked list and return it.

💡 Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = []
Output: []

🧩 Approach (Divide and Conquer):
1. Pair lists two by two and merge them using mergeTwoLists.
2. Repeat the process until only one merged list remains.
3. mergeTwoLists merges two sorted linked lists iteratively.

⏱️ Time Complexity:  O(N log k)  # N = total nodes, k = number of lists
💾 Space Complexity: O(1)        # iterative merge, extra space negligible
------------------------------------------------------------
"""
from typing import List, Optional


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return res.next

if __name__ == "__main__":
    s = Solution()

    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    result = s.mergeKLists(lists = [head1, head2, head3])

    printList(result)


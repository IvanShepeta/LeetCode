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


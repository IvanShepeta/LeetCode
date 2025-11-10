"""
------------------------------------------------------------
🧠 Problem: 2. Add Two Numbers
🔗 Link: https://leetcode.com/problems/add-two-numbers/
------------------------------------------------------------
📜 Description:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

💡 Example:
l1 = [2,4,3], l2 = [5,6,4]
addTwoNumbers(l1, l2) → [7,0,8]
Explanation: 342 + 465 = 807.

🧩 Approach:
Use a dummy head node to simplify list construction.
Iterate through both lists, summing corresponding nodes and carry.

⏱️ Time Complexity:  O(max(m,n))
💾 Space Complexity: O(max(m,n))
------------------------------------------------------------
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10

            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

# 🔧 Допоміжна функція: створює ListNode зі звичайного списку
def list_to_listnode(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# 🔧 Допоміжна функція: перетворює ListNode назад у звичайний список
def listnode_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


# 🚀 Приклад використання
l1 = list_to_listnode([2, 4, 3])
l2 = list_to_listnode([5, 6, 4])

s = Solution()
result = s.addTwoNumbers(l1, l2)
print(listnode_to_list(result))
"""
------------------------------------------------------------
🧠 Problem: 20. Valid Parentheses
🔗 Link: https://leetcode.com/problems/valid-parentheses/
------------------------------------------------------------
📜 Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A valid string must:
 - Have matching opening & closing brackets
 - Follow correct order (proper nesting)

💡 Example:
Input: s = "()"
Output: True

Input: s = "(]"
Output: False

Input: s = "([{}])"
Output: True

🧩 Approach (Stack):
1. Use a stack to store opening brackets.
2. When encountering a closing bracket, check whether it matches
   the type at the top of the stack.
3. If mismatch -> invalid.
4. At the end, stack must be empty.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(n)
------------------------------------------------------------
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else: return False
            else:
                stack.append(c)
        return not stack



s = Solution()
print(s.isValid("()")) # Output: true
print(s.isValid("()[]{}")) # Output: true
print(s.isValid("(]")) # Output: false
print(s.isValid("([])")) # Output: true
print(s.isValid("([)]")) # Output: false

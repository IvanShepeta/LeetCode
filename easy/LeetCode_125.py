"""
------------------------------------------------------------
🧠 Problem: 125. Valid Palindrome
🔗 Link: https://leetcode.com/problems/valid-palindrome/
------------------------------------------------------------
📜 Description:
A phrase is a palindrome if, after converting all uppercase
letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward.

Return True if it is a palindrome, otherwise False.

💡 Example:
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False

🧩 Approach (Two Pointers):
1. Clean string: keep only alphanumeric characters and lowercase them.
2. Use two pointers (left/right) to compare characters.
3. Move inward until mismatch or pointers cross.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1) (ignoring cleaned copy)
------------------------------------------------------------
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama")) # Output: true
print(s.isPalindrome(s = "race a car")) # Output: false
print(s.isPalindrome(s = " ")) # Output: true
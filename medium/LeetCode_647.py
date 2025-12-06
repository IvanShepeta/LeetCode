"""
------------------------------------------------------------
🧠 Problem: 647. Palindromic Substrings
🔗 Link: https://leetcode.com/problems/palindromic-substrings/
------------------------------------------------------------
📜 Description:
Given a string s, return the number of palindromic substrings in it.
A substring is palindromic if it reads the same forward and backward.

💡 Example:
Input: "abc"
Output: 3  (each character is a palindrome)

Input: "aaa"
Output: 6
- "a" (3 times)
- "aa" (2 times)
- "aaa" (1 time)

🧩 Approach (Expand Around Center):
For each index:
    - expand around single character (odd-length palindromes)
    - expand around two characters (even-length palindromes)
While expanding, count valid palindromes.

⏱️ Time Complexity:  O(n²)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def count(left, right):
            nonlocal res
            while left >=0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            count(i, i)
            count(i, i + 1)

        return res

s = Solution()

assert s.countSubstrings("abc") == 3
assert s.countSubstrings("aaa") == 6
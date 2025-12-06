"""
------------------------------------------------------------
🧠 Problem: 5. Longest Palindromic Substring
🔗 Link: https://leetcode.com/problems/longest-palindromic-substring/
------------------------------------------------------------
📜 Description:
Given a string s, return the longest palindromic substring in s.

💡 Examples:
Input: s = "babad"
Output: "bab" or "aba"

Input: s = "cbbd"
Output: "bb"

🧩 Approach (Expand Around Center):
1. A palindrome mirrors around its center.
2. For each index, expand outward for:
   - Odd-length palindromes (center at one char)
   - Even-length palindromes (center between two chars)
3. Track the longest valid palindrome found.

⏱️ Time Complexity:  O(n²)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def cal(left, right):
            nonlocal resLen, res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            cal(i, i)
            cal(i, i + 1)

        return res


s = Solution()

assert s.longestPalindrome("babad") == "bab"
assert s.longestPalindrome("cbbd") == "bb"
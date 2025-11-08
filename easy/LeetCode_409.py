"""
------------------------------------------------------------
🧠 Problem: 409. Longest Palindrome
🔗 Link: https://leetcode.com/problems/longest-palindrome/
------------------------------------------------------------
📜 Description:
Given a string `s`, return the length of the longest palindrome
that can be built with the letters of `s`.

💡 Example:
Input:  s = "abccccdd"
Output: 7  ("dccaccd")

🧩 Approach:
- Count frequency of each letter.
- Even counts contribute fully.
- Odd counts contribute `count - 1`.
- Add +1 if any odd count exists (center letter).

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_letter = {}
        for k in s:
            count_letter[k] = count_letter.get(k, 0) + 1
        r = 0
        add = False
        for k in count_letter:
            if count_letter[k] % 2 == 0:
                r += count_letter[k]
            else:
                r += count_letter[k] - 1
                add = True
        if add:
            r += 1
        return r



s = Solution()
result = s.longestPalindrome("abccccdd")
print(result)
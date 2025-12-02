"""
------------------------------------------------------------
🧠 Problem: 424. Longest Repeating Character Replacement
🔗 Link: https://leetcode.com/problems/longest-repeating-character-replacement/
------------------------------------------------------------
📜 Description:
You are given a string s and an integer k.
You may replace at most k characters in the string so that the
resulting substring contains repeating characters only.
Return the length of the longest possible substring.

💡 Example:
Input: s = "ABAB", k = 2
Output: 4

Input: s = "AABABBA", k = 1
Output: 4

🧩 Approach (Sliding Window + Frequency Counting):
1. Use a sliding window that expands over the string.
2. Track counts of characters inside the window.
3. Keep track of the most frequent character count in the window.
4. If window length - max_freq > k,
   → shrink left side since more than k replacements required.
5. Update maximum window length found.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)   # only 26 uppercase letters
------------------------------------------------------------
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.characterReplacement(s = "ABAB", k = 2))
print(s.characterReplacement(s = "AABABBA", k = 1))
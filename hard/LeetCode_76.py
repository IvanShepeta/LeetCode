"""
------------------------------------------------------------
🧠 Problem: 76. Minimum Window Substring
🔗 Link: https://leetcode.com/problems/minimum-window-substring/
------------------------------------------------------------
📜 Description:
Given two strings s and t, return the minimum window substring
of s such that every character in t (including duplicates)
appears in the window. If no such substring exists, return "".

💡 Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "aa"
Output: ""

🧩 Approach (Sliding Window + Frequency Counter):
1. Use two hashmaps:
   - `need` to count required characters from t
   - `window` to track characters inside current window
2. Expand right pointer to include characters
3. Once a valid window is found, shrink from the left to minimize it
4. Keep track of the best (shortest) valid window

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1) — bounded by character set size
------------------------------------------------------------
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass



s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))  # Output: "BANC"
print(s.minWindow(s = "a", t = "aa"))  # Output: "aa"
print(s.minWindow( s = "a", t = "a"))  # Output: "a"
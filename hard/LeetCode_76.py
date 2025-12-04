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
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("inf")
        l = 0
        have, need = 0, len(countT)


        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""


s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))  # Output: "BANC"
print(s.minWindow(s = "a", t = "aa"))  # Output: ""
print(s.minWindow( s = "a", t = "a"))  # Output: "a"
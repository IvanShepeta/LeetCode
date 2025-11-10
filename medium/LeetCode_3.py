"""
------------------------------------------------------------
🧠 Problem: 3. Longest Substring Without Repeating Characters
🔗 Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
------------------------------------------------------------
📜 Description:
Given a string s, find the length of the longest substring without repeating characters.

💡 Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

🧩 Approach:
Use the sliding window technique with a set or dictionary to track characters.
Move the right pointer to expand the window and left pointer to shrink when duplicates appear.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(min(n, charset))
------------------------------------------------------------
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        d = {}
        start = 0
        for end in range(len(s)):
            if s[end] in d:
                start = max(start, d[s[end]] + 1)
            d[s[end]] = end
            result = max(result, end - start + 1)
        return result

s = Solution()
result = s.lengthOfLongestSubstring(s = "pwwkew")
print(result)

"""
------------------------------------------------------------
🧠 Problem: 49. Group Anagrams
🔗 Link: https://leetcode.com/problems/group-anagrams/
------------------------------------------------------------
📜 Description:
Given an array of strings, group the strings that are anagrams —
words that contain the same characters in different order.

💡 Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

🧩 Approach (Hash Map with Sorted Signature):
1. Create a dictionary where key = sorted string, value = list of anagrams.
2. For each word:
   - Sort its characters (e.g., "eat" → "aet")
   - Append word to dictionary group under this key
3. Return dictionary values as grouped result.

⏱️ Time Complexity:  O(n * k log k)
    n — number of strings
    k — average string length (sorting cost)
💾 Space Complexity: O(n * k)
------------------------------------------------------------
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        #
        # for s in strs:
        #     count = [0] * 26
        #     for char in s:
        #         count[ord(char)- ord("a")] += 1
        #     res[tuple(count)].append(s)
        # return res.values()
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



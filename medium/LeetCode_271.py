"""
------------------------------------------------------------
🧠 Problem: 271. Encode and Decode Strings
🔗 Link: https://leetcode.com/problems/encode-and-decode-strings/
------------------------------------------------------------
📜 Description:
Design an algorithm to encode a list of strings to a single
string and decode it back to the original list of strings.

The encoded string should be able to handle any characters,
including special characters like '#', '/', etc.

💡 Example:
Input: ["lint","code","love","you"]
Encoded: "4#lint4#code4#love3#you"
Decoded: ["lint","code","love","you"]

🧩 Approach (Length Prefix Encoding):
1. For each string, prepend its length followed by a delimiter '#'.
2. Concatenate all encoded strings into one.
3. While decoding:
   - Read the length before '#'
   - Extract the next `length` characters as one string
   - Repeat until the end

⏱️ Time Complexity:
- Encode: O(n)
- Decode: O(n)

💾 Space Complexity: O(1) extra (excluding output)
------------------------------------------------------------
"""
import pytest
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res


codec = Solution()
data = ["lint", "code", "love", "you"]
assert codec.decode(codec.encode(data)) == data


data = ["", "", ""]
assert codec.decode(codec.encode(data)) == data


data = ["#", "##", "a#b#c"]
assert codec.decode(codec.encode(data)) == data

data = []
assert codec.decode(codec.encode(data)) == data

data = ["hello"]
assert codec.decode(codec.encode(data)) == data
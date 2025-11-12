"""
------------------------------------------------------------
🧠 Problem: 190. Reverse Bits
🔗 Link: https://leetcode.com/problems/reverse-bits/
------------------------------------------------------------
📜 Description:
Reverse the bits of a given 32 bits unsigned integer.

💡 Example:
Input:  n = 43261596   (0b00000010100101000001111010011100)
Output: 964176192      (0b00111001011110000010100101000000)

🧩 Approach:
Two common approaches:

1️⃣ String method (simple, less efficient):
- Convert number to binary string: bin(n)[2:]
- Pad with leading zeros to 32 bits: zfill(32)
- Reverse string: [::-1]
- Convert back to integer: int(reversed_string, 2)
- Works but involves string operations.

2️⃣ Bit manipulation (efficient):
- Initialize result = 0
- For each bit position i in 0..31:
    - Extract bit: (n >> i) & 1
    - Place bit at reversed position: bit << (31 - i)
    - Combine with result: res |= bit << (31 - i)
- Returns the reversed bits as integer.

⏱️ Time Complexity: O(32) = O(1)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        # n = bin(n)[2:].zfill(32)[::-1]
        # return int(n,2)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit <<(31 - i))
        return res

s = Solution()
print(s.reverseBits(43261596))
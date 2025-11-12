"""
------------------------------------------------------------
🧠 Problem: 191. Number of 1 Bits
🔗 Link: https://leetcode.com/problems/number-of-1-bits/
------------------------------------------------------------
📜 Description:
Write a function that takes an unsigned integer and returns
the number of '1' bits it has (also known as the Hamming weight).

💡 Example:
Input:  n = 11   # binary: 1011
Output: 3

🧩 Approach:
Two common approaches:
1. Convert to binary string and sum the bits:
   - Convert n to binary using bin(n)
   - Strip '0b' prefix and sum integer values of bits
2. Bit manipulation:
   - Use n & 1 to check the last bit
   - Right-shift n until it becomes 0
   - Count the number of 1s encountered

⏱️ Time Complexity:  O(log n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = bin(n)[2:]
        # return sum(int(bit) for bit in res)
        # return bin(n).count('1')
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


s = Solution()
print(s.hammingWeight(n = 11))
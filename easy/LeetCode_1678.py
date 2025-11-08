"""
------------------------------------------------------------
🧠 Problem: 1678. Goal Parser Interpretation
🔗 Link: https://leetcode.com/problems/goal-parser-interpretation/
------------------------------------------------------------
📜 Description:
You are given a string command containing "G", "()", and "(al)".
Interpret it as:
- "G" → "G"
- "()" → "o"
- "(al)" → "al"

💡 Example:
Input:  command = "G()(al)"
Output: "Goal"

🧩 Approach:
Use string replace operations.

⏱️ Time Complexity:  O(n)
💾 Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution:
    def interpret(self, command: str) -> str:
        print(command)
        return command.replace("()", "o").replace("(al)", "al")

s = Solution()
result = s.interpret("G()(al)")
print(result)

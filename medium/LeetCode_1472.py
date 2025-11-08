"""
------------------------------------------------------------
🧠 Problem: 1472. Design Browser History
🔗 Link: https://leetcode.com/problems/design-browser-history/
------------------------------------------------------------
📜 Description:
Design a browser history system that supports:
- visit(url): visit a new page
- back(steps): go back up to 'steps' pages
- forward(steps): go forward up to 'steps' pages

💡 Example:
bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.back(1)   → "google.com"
bh.forward(1) → "facebook.com"

🧩 Approach:
Use a list and a pointer (index) to simulate history.
Clear forward pages when visiting a new URL.

⏱️ Time Complexity:  O(steps) for back/forward
💾 Space Complexity: O(n)
------------------------------------------------------------
"""

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.last_index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.last_index + 1]
        self.history.append(url)
        self.last_index += 1

    def back(self, steps: int) -> str:
        self.last_index = max(0, self.last_index - steps)
        return self.history[self.last_index]

    def forward(self, steps: int) -> str:
        self.last_index = min(len(self.history)-1, self.last_index + steps)
        return self.history[self.last_index]

# Your BrowserHistory object will be instantiated and called as such:
bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
print(bh.back(1))      # facebook.com
print(bh.back(1))      # google.com
print(bh.forward(1))   # facebook.com
bh.visit("linkedin.com")
print(bh.forward(2))   # linkedin.com
print(bh.back(2))      # google.com
print(bh.back(7))      # leetcode.com

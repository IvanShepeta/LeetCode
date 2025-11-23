"""
------------------------------------------------------------
🧠 Problem: 269. Alien Dictionary
🔗 Link: https://leetcode.com/problems/alien-dictionary/
------------------------------------------------------------
📜 Description:
Given a list of words from an alien language, find the order of letters in the language.
All letters are lowercase English letters. If no valid order exists, return "".

💡 Example:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation:
- "wrt" < "wrf" → t before f
- "wrf" < "er"  → w before e
- "er" < "ett"  → r before t
- "ett" < "rftt" → e before r

🧩 Approach (Graph + DFS Topological Sort):
1️⃣ Build a directed graph of character dependencies:
    - For each pair of adjacent words, find the first differing character.
    - Add an edge from the character in the first word to the character in the second word.
    - Handle invalid cases where a longer word is a prefix of a shorter word.
2️⃣ Perform DFS to detect cycles and generate topological order.
    - True in `visit` → node in current DFS path → cycle
    - False → node fully processed
3️⃣ Reverse the DFS post-order to get correct character order.

⏱️ Time Complexity:  O(C)  (C = total number of characters in all words)
💾 Space Complexity: O(C + D)  (D = number of edges in the graph)
------------------------------------------------------------
"""
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False=visited, True=current path
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for w in adj[c]:
                if dfs(w):
                    return True

            visit[c] = False
            res.append(c)


        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

solution = Solution()
print(solution.alienOrder(["wrt","wrf","er","ett","rftt"])) # Output: "wertf"

def test_alien_dictionary_hard():
    solution = Solution()

    # Test 1: Large linear chain
    words1 = ["a", "b", "c", "d", "e", "f", "g"]
    assert solution.alienOrder(words1) == "abcdefg", "Test 1 Failed"

    # Test 2: Multiple valid orders
    words2 = ["abc", "abd", "bce", "bdf"]
    # Valid topological orders: 'abcdef', 'abdcfe', etc.
    result2 = solution.alienOrder(words2)
    for char in "abcdef":
        assert char in result2, "Test 2 Failed"

    # Test 3: Cycle in the graph (no valid order)
    words3 = ["a","b","c","a"]
    assert solution.alienOrder(words3) == "", "Test 3 Failed"

    # Test 4: Prefix invalid case
    words4 = ["abc","ab","abcd"]
    assert solution.alienOrder(words4) == "", "Test 4 Failed"

    # Test 5: Disconnected characters
    words5 = ["wrt","wrf","er","ett","rftt","xyz"]
    # 'x', 'y', 'z' are disconnected and can appear anywhere
    result5 = solution.alienOrder(words5)
    for char in "wertfxyz":
        assert char in result5, "Test 5 Failed"

    # Test 6: Large graph with multiple constraints
    words6 = ["za","zb","ca","cb"]
    # Constraints: z->c, a->b; valid order: zacb or zcab
    result6 = solution.alienOrder(words6)
    for char in "zacb":
        assert char in result6, "Test 6 Failed"

    print("✅ All hard tests passed!")

if __name__ == "__main__":
    test_alien_dictionary_hard()
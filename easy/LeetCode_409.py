#TODO Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_letter = {}
        for k in s:
            count_letter[k] = count_letter.get(k, 0) + 1
        r = 0
        add = False
        for k in count_letter:
            if count_letter[k] % 2 == 0:
                r += count_letter[k]
            else:
                r += count_letter[k] - 1
                add = True
        if add:
            r += 1
        return r



s = Solution()
result = s.longestPalindrome("abccccdd")
print(result)
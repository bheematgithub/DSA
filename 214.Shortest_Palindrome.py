class Solution:
    def shortestPalindrome(self, s: str) -> str:
        mtch = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(mtch[i:]):
                return mtch[:i] + s

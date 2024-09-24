class Solution:
    def longestPalindrome(self, s: str) -> int:
        cSet = set()
        res = 0

        for char in s:
            if char in cSet:
                res += 2
                cSet.remove(char)
            else:
                cSet.add(char)

        if cSet:
            res += 1

        return res

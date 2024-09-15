class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == ")":
                l.pop()
                if len(l) == 0:
                    l.append(i)
                else:
                    res = max(res, i - l[-1])
            else:
                l.append(i)
        return res

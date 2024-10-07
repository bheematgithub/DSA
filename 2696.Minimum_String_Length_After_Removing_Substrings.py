class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                i=s.find("AB")
            else:
                i=s.find("CD")
            s=s[:i]+s[i+2:]
        return len(s)

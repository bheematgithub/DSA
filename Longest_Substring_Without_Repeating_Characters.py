class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        l,r=0,1
        res=1
        sets=set(s[l])

        while r<len(s):
            
            while s[r] in sets :
                sets.remove(s[l])
                l+=1
            sets.add(s[r])
            res=max(res,len(sets))
            r+=1

        return res

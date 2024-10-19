class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=""
        for i in s:
            res+=str(ord(i)-96)
        sm=0
        for _ in range(k):
            sm=0
            for j in res:
                sm+=int(j)
            res=str(sm)

        return sm

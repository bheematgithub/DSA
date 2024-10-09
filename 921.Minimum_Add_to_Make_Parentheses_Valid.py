class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a,b=0,0

        for i in s:
            if i=="(":
                a+=1
            elif i==")" and a>0:
                a-=1
            else:
                b+=1

        return a+b

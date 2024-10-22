class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,h=0,int((c+1)**0.5)
        while l<=h:
            x= l**2 + h**2
            if x==c:
                return True
            elif x<c:
                l+=1
            else:
                h-=1
        return False

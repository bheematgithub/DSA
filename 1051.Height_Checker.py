class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l,c=sorted(heights),0
        for i,n in enumerate(l):
            if n!=heights[i]:
                c+=1
        return c

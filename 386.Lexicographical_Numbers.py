class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=[str(i+1) for i in range(n)]
        l.sort()
        return [int(l[i]) for i in range(n)]

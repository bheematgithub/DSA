class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res=[]

        sm=(len(rolls)+n)*mean-sum(rolls)

        if sm <= n*6 and sm >= n:
            base = sm//n
            rmdr = sm % n
            res = [base] * n
            for i in range(rmdr):
                res[i] += 1
                
        return res

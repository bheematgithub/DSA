class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])

        if r*c != m*n:
            return mat

        el=[]
        for i in range(m):
            el.extend(mat[i])

        res=[]
        for i in range(r):
            res.append(el[c*i:c*i+c])

        return res

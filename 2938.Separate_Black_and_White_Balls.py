class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        blk = 0 

        for i in s:
            if i == '0':
                res += blk
            else:
                blk += 1

        return res

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res=skill[0] * skill[-1]
        team=skill.pop(0)+skill.pop()
        n=len(skill)

        for i in range(n//2):
            if skill[i]+skill[n-i-1]!=team:
                return -1
            else:
                res+=skill[i]*skill[n-i-1]

        return res

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm=sum(chalk)
        rem =k%sm
        for i in range(len(chalk)):
            if rem >= chalk[i]:
                rem -= chalk[i]
            else :
                return i
        return 0

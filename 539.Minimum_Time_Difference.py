class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res = 1440 + (int(timePoints[0][:2]) * 60 + int(timePoints[0][3:])) - (int(timePoints[-1][:2]) * 60 + int(timePoints[-1][3:]))

        for i in range(1, len(timePoints)):
            if res == 0:
                return 0
            pr = int(timePoints[i-1][:2]) * 60 + int(timePoints[i-1][3:])
            cu = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])
            res = min(res, cu - pr)

        return res

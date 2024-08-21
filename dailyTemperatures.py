class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stk = []
        ans = [0] * n

        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                idx = stk.pop()
                ans[idx] = i - idx
            stk.append(i)
        
        return ans

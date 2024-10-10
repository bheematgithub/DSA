class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        stk = []
        n=len(nums)
        for i in range(n):
            if not stk or nums[stk[-1]] > nums[i]:
                stk.append(i)

        for j in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] <= nums[j]:
                res = max(res, j - stk.pop())

        return res

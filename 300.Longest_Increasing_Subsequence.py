class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        i,j=0,0
        while j<n:
            if nums[i]<nums[j]:
                if (dp[i]+1)>dp[j]:
                    dp[j]=dp[i]+1
            if i==j:
                i=0
                j+=1
            else:
                i+=1
        return max(dp)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        ps = 0
        ha = {0: 1}
        
        for num in nums:
            ps += num
            if (ps - k) in ha:
                c += ha[ps - k]
            if ps in ha:
                ha[ps] += 1
            else:
                ha[ps] = 1 
        return c

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem=sum(nums)%p
        if rem == 0:
            return 0

        n=len(nums)
        hmap={0:-1}
        psum=0

        for i,num in enumerate(nums):
            psum+=num
            mod=psum%p
            target=(mod-rem+p)%p
            if target in hmap:
                n=min(n,i-hmap[target])

            hmap[mod]=i
        return n if n<len(nums) else -1

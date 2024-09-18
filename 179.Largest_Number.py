class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = [str(i) for i in nums]
        l.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        res = ''.join(l)
        return '0' if res[0] == '0' else res

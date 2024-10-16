class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = {i: 0 for i in arr2}
        rem = []

        for n in arr1:
            if n in cnt:
                cnt[n] += 1
            else:
                rem.append(n)

        res = []
        for n in arr2:
            res.extend([n] * cnt[n])

        res.extend(sorted(rem))
        return res

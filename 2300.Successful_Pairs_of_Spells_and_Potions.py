class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        n = len(potions)
        for i in spells:
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) >> 1
                if potions[mid] * i >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            res.append(n - l)
        return res

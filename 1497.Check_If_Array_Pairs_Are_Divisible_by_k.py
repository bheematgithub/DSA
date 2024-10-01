class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = [0] * k

        for n in arr:
            rm = (n % k + k) % k
            f[rm] += 1

        if f[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if f[i] != f[k - i]:
                return False

        return True

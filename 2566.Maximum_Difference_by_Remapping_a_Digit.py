class Solution:
    def minMaxDifference(self, num: int) -> int:
        ns=str(num)
        mx=ns
        for i in ns:
            if i != "9":
                mx=ns.replace(i,"9")
                break
        mn=ns.replace(ns[0],"0")
        return int(mx)-int(mn)

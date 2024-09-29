class AllOne:

    def __init__(self):
        self.dic={}

    def inc(self, key: str) -> None:
        if key in self.dic:
            self.dic[key]+=1
        else:
            self.dic[key]=1

    def dec(self, key: str) -> None:
        self.dic[key]-=1
        if self.dic[key]==0:
            self.dic.pop(key)

    def getMaxKey(self) -> str:
        if self.dic:
            return max(self.dic, key=lambda k: self.dic[k])
        return ""

    def getMinKey(self) -> str:
        if self.dic:
            return min(self.dic, key=lambda k: self.dic[k])
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

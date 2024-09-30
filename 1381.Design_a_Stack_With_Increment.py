class CustomStack:

    def __init__(self, maxSize: int):
        self.stk=[]
        self.size=maxSize
        self.ct=0

    def push(self, x: int) -> None:
        if self.ct<self.size:
            self.stk.append(x)
            self.ct+=1

    def pop(self) -> int:
        if self.stk:
            self.ct-=1
            return self.stk.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.ct)):
            self.stk[i]+=val      


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

class MyCalendarTwo:

    def __init__(self):
        self.cal = []
        self.olp = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.olp:
            if start < j and end > i:
                return False

        for i, j in self.cal:
            if start < j and end > i:
                self.olp.append((max(start, i), min(end, j)))
        self.cal.append((start, end))

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

# Last updated: 7/12/2025, 11:55:31 PM
class MyCalendarTwo:

    def __init__(self):
        self.non_overlapping = []
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        
        for s, e in self.overlapping:
            if end > s and e > start:
                return False

        for s, e in self.non_overlapping:
            if end > s and e > start:
                self.overlapping.append(
                    (max(start,s),min(end,e))
                )
        self.non_overlapping.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
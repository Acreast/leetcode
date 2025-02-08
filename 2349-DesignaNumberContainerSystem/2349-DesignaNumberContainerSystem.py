from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index_val = {}  # Maps index -> number
        self.res = {}  # Maps number -> SortedSet of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_val:
            prev_number = self.index_val[index]
            if prev_number == number:
                return
            self.res[prev_number].discard(index)
            if not self.res[prev_number]:  # Clean up empty sets
                del self.res[prev_number]

        if number not in self.res:
            self.res[number] = SortedSet()
        self.res[number].add(index)
        self.index_val[index] = number

    def find(self, number: int) -> int:
        if number not in self.res or not self.res[number]:
            return -1
        return self.res[number][0]  # O(1) time to get min value

# Usage
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)

# Last updated: 7/12/2025, 11:51:47 PM
class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = []
            self.prod = 1
        else:
            self.prod *= num
            self.stream.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.stream) < k:
            return 0
        if len(self.stream) == k:
            return self.stream[-1]
        return self.stream[-1] // self.stream[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
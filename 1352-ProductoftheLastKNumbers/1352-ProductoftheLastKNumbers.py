# Last updated: 11/23/2026, 11:29:35 PM
1class ProductOfNumbers:
2
3    def __init__(self):
4        self.arr = []
5        self.prod = 1
6
7    def add(self, num: int) -> None:
8        if num == 0:
9            self.arr = []
10            self.prod = 1
11        else:
12            self.prod *= num
13            self.arr.append(self.prod)
14
15    def getProduct(self, k: int) -> int:
16        if len(self.arr) < k:
17            return 0
18        if len(self.arr) == k:
19            return self.arr[-1]
20        return self.arr[-1] // self.arr[-k-1]
21
22
23
24# Your ProductOfNumbers object will be instantiated and called as such:
25# obj = ProductOfNumbers()
26# obj.add(num)
27# param_2 = obj.getProduct(k)
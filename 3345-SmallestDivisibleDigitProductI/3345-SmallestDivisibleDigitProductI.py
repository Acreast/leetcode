# Last updated: 8/7/2026, 12:54:37 AM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        while True:
4            
5            prod = n % 10
6            cur = n // 10
7            while cur > 0:
8                prod *= cur % 10
9                cur //= 10
10            if prod % t == 0:
11                return n
12            n += 1
13        return 0
14
15
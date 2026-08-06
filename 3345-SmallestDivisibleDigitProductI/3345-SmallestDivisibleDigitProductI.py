# Last updated: 8/7/2026, 12:54:11 AM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        while True:
4            
5            prod = n % 10
6            cur = n // 10
7            while cur > 0:
8                digit = cur % 10
9                prod *= digit
10                cur //= 10
11            if prod % t == 0:
12                return n
13            n += 1
14        return 0
15
16
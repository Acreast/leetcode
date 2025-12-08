# Last updated: 12/8/2025, 8:49:06 PM
1class Solution:
2    def countTriples(self, n: int) -> int:
3        squares = {i*i: i for i in range(1, n+1)}
4        res = 0
5        for a in range(1, n+1):
6            for b in range(1, n+1):
7                if a*a + b*b in squares:
8                    res += 1
9        return res
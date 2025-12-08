# Last updated: 12/8/2025, 8:48:09 PM
1class Solution:
2    def countTriples(self, n: int) -> int:
3        res = 0
4        for a in range(1, n+1):
5            for b in range(1, n+1):
6                c2 = a*a + b*b
7                c = int(c2**0.5)
8                if c <= n and c*c == c2:
9                    res += 1
10        return res
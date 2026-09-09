# Last updated: 9/9/2026, 10:40:30 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        res = 0
4        p = 1000
5
6        while p <= n:
7            res += n - p + 1
8            p *= 1000
9
10        return res
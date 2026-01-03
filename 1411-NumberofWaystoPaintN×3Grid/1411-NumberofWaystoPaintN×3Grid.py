# Last updated: 1/3/2026, 10:23:08 PM
1class Solution:
2    def numOfWays(self, n: int) -> int:
3        MOD = 10 ** 9 + 7
4        A = 6
5        B = 6
6        for i in range(2, n + 1):
7            newA = (2 * A + 2 * B) % MOD
8            newB = (2 * A + 3 * B) % MOD
9            A = newA
10            B = newB
11        return (A + B) % MOD
12
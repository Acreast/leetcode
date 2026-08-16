# Last updated: 8/17/2026, 1:16:21 AM
1class Solution:
2    def stoneGameIX(self, stones: List[int]) -> bool:
3        f = [0, 0, 0]
4
5        for s in stones:
6            f[s % 3] += 1
7
8        if ~f[0] & 1:
9            return min(f[1], f[2]) >= 1
10
11        return abs(f[1] - f[2]) >= 3
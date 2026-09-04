# Last updated: 9/5/2026, 2:01:13 AM
1suf = [0] * 100
2class Solution:
3    def firstStableIndex(self, A: list[int], k: int) -> int:
4        n = len(A)        
5        suf[n - 1] = A[-1]
6
7        for i in range(n - 2, -1, -1):
8            suf[i] = min(suf[i + 1], A[i])
9
10        mx = 0
11        for i, x in enumerate(A):
12            mx = max(mx, x)
13            if mx - suf[i] <= k:
14                return i
15
16        return -1
# Last updated: 9/5/2026, 5:28:33 PM
1
2class Solution:
3    def firstStableIndex(self, A: list[int], k: int) -> int:
4        suf = [0] * (len(A) + 1)
5        n = len(A)        
6        suf[n - 1] = A[-1]
7
8        for i in range(n - 2, -1, -1):
9            suf[i] = min(suf[i + 1], A[i])
10
11        mx = 0
12        for i, x in enumerate(A):
13            mx = max(mx, x)
14            if mx - suf[i] <= k:
15                return i
16
17        return -1
# Last updated: 8/4/2026, 12:39:54 AM
1class Solution:
2    def stoneGameIII(self, A: List[int]) -> str:
3        s = [ "Bob", "Tie", "Alice"]
4        n = len(A)
5
6        @cache
7        def maxDiff(i):
8            if i == n : return 0
9            a = b = c = -5e7
10
11            if i < n:
12                a = A[i] - maxDiff(i + 1)
13            if i + 1 < n:
14                b = A[i] + A[i + 1] - maxDiff(i + 2)
15            if i + 2 < n:
16                c = A[i] + A[i + 1] + A[i + 2] - maxDiff(i + 3)
17            
18            return max(a,b,c)
19
20        d = maxDiff(0)
21
22        return s[(d > 0) - (d < 0) + 1]
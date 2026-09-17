# Last updated: 9/18/2026, 12:15:56 AM
1class Solution:
2    def minSumOfLengths(self, A: List[int], k: int) -> int:
3        n = len(A)
4        res, tot, i = n + 1, 0, 0
5
6        dp = [n] * (n + 1)
7
8        for j in range(n):
9            tot += A[j]
10
11            while tot > k:
12                tot -= A[i]
13                i += 1
14            dp[j + 1] = dp[j]
15
16            if tot == k:
17                res = min(res, j - i + 1 + dp[i])
18                dp[j + 1] = min(dp[j], j - i + 1)
19
20        return -1 if res == n + 1 else res
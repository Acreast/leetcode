# Last updated: 1/11/2026, 1:41:01 AM
1class Solution:
2    def minimumDeleteSum(self, s1: str, s2: str) -> int:
3        n, m = len(s1), len(s2)
4
5        # dp[i][j] = maximum ASCII sum of common subsequence
6        dp = [[0] * (m + 1) for _ in range(n + 1)]
7
8        for i in range(n):
9            for j in range(m):
10                if s1[i] == s2[j]:
11                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
12                else:
13                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
14
15        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
16        return total_ascii - 2 * dp[n][m]
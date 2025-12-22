# Last updated: 12/23/2025, 12:47:25 AM
1class Solution:
2    def minDeletionSize(self, strs: list[str]) -> int:
3        m = len(strs[0])
4        dp = [1] * m
5
6        for i in range(m):
7            for j in range(i):
8                if all(row[j] <= row[i] for row in strs):
9                    dp[i] = max(dp[i], dp[j] + 1)
10
11        return m - max(dp)
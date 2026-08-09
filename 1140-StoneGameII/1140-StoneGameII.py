# Last updated: 8/10/2026, 12:34:13 AM
1class Solution:
2    def stoneGameII(self, piles: List[int]) -> int:
3        n = len(piles)
4        
5        dp = [[0] * (n + 1) for _ in range(n)]
6        suffix_sum = [0] * n
7        suffix_sum[-1] = piles[-1]
8        
9        for i in range(n - 2, -1, -1):
10            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
11        
12        for i in range(n - 1, -1, -1):
13            for m in range(1, n + 1):
14                if i + 2 * m >= n:
15                    dp[i][m] = suffix_sum[i]
16                else:
17                    for x in range(1, 2 * m + 1):
18                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])
19        
20        return dp[0][1]
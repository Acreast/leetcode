# Last updated: 12/17/2025, 10:02:28 PM
1class Solution:
2    def maximumProfit(self, prices: List[int], k: int) -> int:
3        res = 0
4        first_price = prices[0]
5        dp = [[0, -first_price, first_price] for _ in range(k + 1)]
6        n = len(prices)
7
8
9        for day in range(1, n):
10            curr_price = prices[day]
11            for trans in range(k, 0, - 1):
12                prev_profit = dp[trans - 1][0]
13                dp[trans][0] = max(dp[trans][0], dp[trans][1] + curr_price, dp[trans][2] - curr_price)
14                dp[trans][1] = max(dp[trans][1], prev_profit - curr_price)
15                dp[trans][2] = max(dp[trans][2], prev_profit + curr_price)
16
17
18        return dp[k][0]
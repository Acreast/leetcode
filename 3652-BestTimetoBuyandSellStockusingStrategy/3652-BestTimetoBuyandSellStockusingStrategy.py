# Last updated: 12/18/2025, 9:39:43 PM
1class Solution:
2    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
3        n = len(strategy)
4        half = k // 2
5
6        base_profit = sum(strategy[i] * prices[i] for i in range(n))
7        res = base_profit
8
9        A = [-strategy[i] * prices[i] for i in range(n)]
10        B = [(1 - strategy[i]) * prices[i] for i in range(n)]
11
12        preA = [0] * (n + 1)
13        preB = [0] * (n + 1)
14
15        for i in range(n):
16            preA[i + 1] = preA[i] + A[i]
17            preB[i + 1] = preB[i] + B[i]
18
19        for l in range(0, n - k + 1):
20            delta = (
21                preA[l + half] - preA[l] +
22                preB[l + k]    - preB[l + half]
23            )
24            res = max(res, base_profit + delta)
25    
26        return res
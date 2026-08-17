# Last updated: 8/18/2026, 12:53:59 AM
1from typing import List
2
3class Solution:
4    def stoneGameV(self, stoneValue: List[int]) -> int:
5        n = len(stoneValue)
6
7        prefix = [0] * (n + 1)
8
9        for i in range(n):
10            prefix[i + 1] = prefix[i] + stoneValue[i]
11
12        dp = [[0] * n for _ in range(n)]
13
14        left_best = [[0] * n for _ in range(n)]
15
16        right_best = [[0] * n for _ in range(n)]
17
18        left_ptr = [0] * n
19
20        right_ptr = list(range(n))
21
22        for i in range(n):
23            left_best[i][i] = stoneValue[i]
24            right_best[i][i] = stoneValue[i]
25
26            left_ptr[i] = i - 1
27
28            right_ptr[i] = i
29
30        for length in range(2, n + 1):
31            for l in range(n - length + 1):
32                r = l + length - 1
33
34                total = prefix[r + 1] - prefix[l]
35
36                while left_ptr[l] + 1 <= r - 1:
37                    k = left_ptr[l] + 1
38                    left_sum = prefix[k + 1] - prefix[l]
39
40                    if 2 * left_sum > total:
41                        break
42
43                    left_ptr[l] += 1
44
45                while right_ptr[l] <= r - 1:
46                    k = right_ptr[l]
47                    left_sum = prefix[k + 1] - prefix[l]
48
49                    if 2 * left_sum >= total:
50                        break
51
52                    right_ptr[l] += 1
53
54                best = 0
55
56                if left_ptr[l] >= l:
57                    best = left_best[l][left_ptr[l]]
58
59                if right_ptr[l] <= r - 1:
60                    best = max(
61                        best,
62                        right_best[right_ptr[l] + 1][r]
63                    )
64
65                dp[l][r] = best
66
67                left_best[l][r] = max(
68                    left_best[l][r - 1],
69                    dp[l][r] + total
70                )
71
72                right_best[l][r] = max(
73                    right_best[l + 1][r],
74                    dp[l][r] + total
75                )
76
77        return dp[0][n - 1]
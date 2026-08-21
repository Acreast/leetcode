# Last updated: 8/22/2026, 1:45:24 AM
1class Solution:
2    def findKthSmallest(self, coins: list[int], k: int) -> int:
3        coins.sort()
4        A = []
5        for c in coins:
6            if all(c % x for x in A):
7                A.append(c)
8
9        n = len(A)
10
11        def check(mid):
12            tot = 0
13            for i in range(1, n + 1):
14                q = (1 << i) - 1
15                lim = 1 << n
16                sgn = ((i & 1) << 1) - 1
17
18                while q < lim:
19                    x = 1
20                    for j in range(n):
21                        if (q >> j) & 1:
22                            x = lcm(x, A[j])
23
24                    tot += (mid // x) * sgn
25
26                    c = q & -q
27                    r = q + c
28                    q = (((r ^ q) >> 2) // c) | r
29            return tot >= k
30
31        return bisect_left(range(A[0] * k + 1), True, lo=k, key=check)
32
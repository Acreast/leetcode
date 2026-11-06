# Last updated: 11/7/2026, 12:51:12 AM
1class Solution:
2    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
3        server, time = zip(*sorted(logs, key=itemgetter(1)), [0, inf])  # split the logs
4        cnt = [0] * (n + 1)  # requests per server inside the window [q - x, q]
5        busy = lo = hi = 0  # servers with at least one request in it
6        ans = [0] * len(queries)
7        for i, q in sorted(enumerate(queries), key=itemgetter(1)):
8            while time[hi] <= q:  # requests up to q come in
9                busy += not cnt[server[hi]]
10                cnt[server[hi]] += 1
11                hi += 1
12            while time[lo] < q - x:  # requests before q - x go out
13                cnt[server[lo]] -= 1
14                busy -= not cnt[server[lo]]
15                lo += 1
16            ans[i] = n - busy
17        return ans
# Last updated: 10/17/2026, 1:05:21 AM
1class Solution:
2    def sumCounts(self, nums: List[int]) -> int:
3        n = len(nums)
4        cnt, tot = [0] * (n + 1), [0] * (n + 1)  # Fenwick trees over previous-copy positions, stored right to left
5        last, ans = {}, 0
6        for r, x in enumerate(nums):
7            p = last.get(x, -1)
8            c = s = 0
9            i = n - p - 1  # boxes 1..n-p-1 hold the positions > p
10            while i:
11                c += cnt[i]
12                s += tot[i]
13                i -= i & -i
14            ans += (n - r) * ((r - p) ** 2 - 2 * (s - p * c))
15            i = n - p  # insert p; p = -1 lands past the end and is skipped
16            while i <= n:
17                cnt[i] += 1
18                tot[i] += p
19                i += i & -i
20            last[x] = r
21        return ans % (10**9 + 7)
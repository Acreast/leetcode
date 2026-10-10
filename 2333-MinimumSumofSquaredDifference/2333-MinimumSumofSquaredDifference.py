# Last updated: 10/11/2026, 2:18:16 AM
1class Solution:
2    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
3        d = [0] * 100001
4        k = k1 + k2
5        total = 0
6        mx = 0
7
8        # Step 1: count the differences
9        for a, b in zip(nums1, nums2):
10            x = abs(a - b)
11            d[x] += 1
12            total += x
13            mx = max(mx, x)
14
15        # Enough budget -> every difference becomes 0
16        if total <= k:
17            return 0
18
19        # Step 2: shave the biggest differences, level by level
20        for i in range(mx, 0, -1):
21            if k <= 0:
22                break
23            move = min(k, d[i])
24            d[i] -= move
25            d[i - 1] += move
26            k -= move
27
28        # Step 3: add up the squares
29        ans = 0
30        for i in range(mx + 1):
31            ans += i * i * d[i]
32
33        return ans
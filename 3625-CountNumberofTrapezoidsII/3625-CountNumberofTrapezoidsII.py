# Last updated: 12/3/2025, 10:41:46 PM
1class Solution:
2    def countTrapezoids(self, points: List[List[int]]) -> int:
3        N = len(points)
4        MOD = 10 ** 9 + 7
5        slope_to_intercept = defaultdict(list)
6        mid_to_slope = defaultdict(list)
7        res = 0
8
9        for i in range(N):
10            x1, y1 = points[i]
11            for j in range(i + 1, N):
12                x2, y2 = points[j]
13                dx = x1 - x2
14                dy = y1 - y2
15
16                if x2 == x1:
17                    k = mod
18                    b = x1
19                else:
20                    k = (y2 - y1) / (x2 - x1)
21                    b = (y1 * dx - x1 * dy) / dx
22
23                mid = (x1 + x2) * 10000 + (y1 + y2)
24                slope_to_intercept[k].append(b)
25                mid_to_slope[mid].append(k)
26            
27        
28        for sti in slope_to_intercept.values():
29            if len(sti) == 1:
30                continue
31            
32            cnt = defaultdict(int)
33            for b_val in sti:
34                cnt[b_val] += 1
35            
36            total_sum = 0
37            for count in cnt.values():
38                res += total_sum * count
39                total_sum += count
40        
41        for mts in mid_to_slope.values():
42            if len(mts) == 1:
43                continue
44            
45            cnt = defaultdict(int)
46            for k_val in mts:
47                cnt[k_val] += 1
48            
49            total_sum = 0
50            for count in cnt.values():
51                res -= total_sum * count
52                total_sum += count
53
54        return res
# Last updated: 8/8/2026, 1:09:57 AM
1import math
2
3class Solution:
4    def smallestNumber(self, num: str, t: int) -> str:
5        temp = t
6        counts = [0, 0, 0, 0]
7        for i, p in enumerate([2, 3, 5, 7]):
8            while temp % p == 0:
9                counts[i] += 1
10                temp //= p
11                
12        if temp > 1:
13            return "-1"
14            
15        divs = []
16        for a in range(counts[0] + 1):
17            for b in range(counts[1] + 1):
18                for c in range(counts[2] + 1):
19                    for d in range(counts[3] + 1):
20                        divs.append((2**a) * (3**b) * (5**c) * (7**d))
21        divs.sort()
22        
23        trans = {v: [v] * 10 for v in divs}
24        for v in divs:
25            for d in range(1, 10):
26                trans[v][d] = v // math.gcd(v, d)
27                
28        dp = {v: float('inf') for v in divs}
29        dp[1] = 0
30        
31        for v in divs:
32            if v == 1:
33                continue
34            best = float('inf')
35            for d in range(2, 10):
36                nxt = trans[v][d]
37                if dp[nxt] + 1 < best:
38                    best = dp[nxt] + 1
39            dp[v] = best
40            
41        n = len(num)
42        first_zero = num.find('0')
43        
44        if first_zero == -1:
45            max_i_allowed = n - 1
46        else:
47            max_i_allowed = first_zero
48            
49        prefix_t = [t]
50        for i in range(max_i_allowed):
51            prefix_t.append(trans[prefix_t[-1]][int(num[i])])
52            
53        if first_zero == -1:
54            full_t = trans[prefix_t[-1]][int(num[-1])]
55            if full_t == 1:
56                return num
57                
58        for i in range(max_i_allowed, -1, -1):
59            p_t = prefix_t[i]
60            rem = n - 1 - i
61            
62            for d in range(int(num[i]) + 1, 10):
63                t_req = trans[p_t][d]
64                if dp[t_req] <= rem:
65                    ans = [num[:i], str(d)]
66                    curr_t = t_req
67                    for step in range(rem):
68                        for nxt_d in range(1, 10):
69                            next_t = trans[curr_t][nxt_d]
70                            if dp[next_t] <= rem - 1 - step:
71                                ans.append(str(nxt_d))
72                                curr_t = next_t
73                                break
74                    return "".join(ans)
75                    
76        length = max(n + 1, dp[t])
77        ans = []
78        curr_t = t
79        for step in range(length):
80            for nxt_d in range(1, 10):
81                next_t = trans[curr_t][nxt_d]
82                if dp[next_t] <= length - 1 - step:
83                    ans.append(str(nxt_d))
84                    curr_t = next_t
85                    break
86        return "".join(ans)
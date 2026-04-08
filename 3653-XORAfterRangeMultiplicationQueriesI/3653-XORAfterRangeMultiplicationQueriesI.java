// Last updated: 4/8/2026, 11:07:28 PM
1class Solution {
2    public int xorAfterQueries(int[] nums, int[][] queries) {
3        int MOD = (int)1e9+7, n = nums.length, m = queries.length;
4
5        int B = (int)Math.sqrt(n);
6
7        ArrayList<int[]> [][] store = new ArrayList[B+1][B+1];
8
9
10        for (int i = 0; i < B; i ++) {
11            for (int j = 0; j < B; j ++) {
12                store[i][j] = new ArrayList<>();
13            }
14        }
15
16        for (int i = 0; i < m; i ++) {
17            int l = queries[i][0], r = queries[i][1];
18            int k = queries[i][2], v = queries[i][3];
19
20            if (k >= B) {
21                for (int idx = l; idx <= r; idx +=k) {
22                    nums[idx] = (int)((1L * nums[idx] * v) % MOD);
23                } 
24            } else {
25                int remainder = l % k;
26                store[k][remainder].add(new int[] {l, r, v});
27            }
28        }
29
30        for (int k = 1; k < B; k++) {   
31            for (int rem = 0; rem < k; rem ++) {
32                if (store[k][rem].isEmpty()) continue;
33
34                ArrayList<int[]> queriesList = store[k][rem];
35
36                int chainLength = (n - rem + k - 1) / k;
37
38                long[] diff = new long[chainLength + 1];
39                Arrays.fill(diff, 1L);
40
41                for (int[] q : queriesList) {
42                    int l = q[0], r = q[1], v = q[2];
43
44                    int startPos = (l - rem) / k;
45                    int endPos = (r - rem) / k;
46                    if (startPos < 0) startPos = 0;
47                    if (endPos >= chainLength) endPos = chainLength - 1;
48                    if (startPos > endPos) continue;
49
50                    diff[startPos] = (diff[startPos] * v) % MOD;
51                    if (endPos + 1 < chainLength) {
52                        diff[endPos + 1] = (diff[endPos + 1] * modInverse(v, MOD)) % MOD;
53                    }
54                }
55
56                long curr = 1L;
57                for (int pos = 0; pos < chainLength; pos ++) {
58                    curr = (curr * diff[pos]) % MOD;
59                    int idx = rem + pos * k;
60                    nums[idx] = (int)((1L * nums[idx] * curr) % MOD);
61                }
62            }
63        }
64
65        int res = 0;
66        for (int i = 0; i < n;i ++) {
67            res ^= nums[i];
68        }
69        return res;
70    }
71
72    private long modInverse(long a, int MOD) {
73        return pow(a, MOD - 2, MOD);
74    }
75
76    private long pow(long a, long b, int MOD) {
77        long result = 1;
78        while (b > 0) {
79            if ((b & 1) == 1) {
80                result = (result * a) % MOD;
81            }
82            a = (a * a) % MOD;
83            b >>= 1;
84        }
85        return result;
86    }
87}
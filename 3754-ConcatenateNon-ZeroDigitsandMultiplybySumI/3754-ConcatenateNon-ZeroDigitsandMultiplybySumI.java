// Last updated: 7/9/2026, 12:30:55 AM
1class Solution {
2    private static final int MOD = 1000000007;
3    private static final int MAX = 100001;
4    private static final int[] pow = new int[MAX];
5
6    static {
7        pow[0] = 1;
8        for (int i = 1; i < MAX; i++)
9            pow[i] = (int) ((pow[i - 1] * 10L) % MOD);
10    }
11
12    public int[] sumAndMultiply(String s, int[][] queries) {
13        int n = s.length();
14        int[] A = new int[n + 1];
15        int[] B = new int[n + 1];
16        int[] len = new int[n + 1];
17
18        for (int i = 0; i < n; i ++) {
19            int d = s.charAt(i) - '0';
20            A[i + 1] = A[i] + d;
21
22            if (d > 0) {
23                B[i + 1] = (int) ((B[i] * 10L + d) % MOD);
24                len[i + 1] = len[i] + 1;
25            } else {
26                B[i + 1] = B[i];
27                len[i + 1] = len[i];
28            }
29        }
30
31        int[] res = new int[queries.length];
32        int i = 0;
33
34        for (int[] q : queries) {
35            int l = q[0], r = q[1] + 1;
36
37            long sub = ((long) B[l] * pow[len[r] - len[l]]) % MOD;
38            long x = (B[r] - sub + MOD) % MOD;
39
40            res[i ++] = (int) ((x * (A[r] - A[l])) % MOD);
41        }        
42
43        return res;
44    }
45}
// Last updated: 2/28/2026, 11:04:18 PM
1class Solution {
2    public int concatenatedBinary(int n) {
3        long res = 0;
4        int MOD = 1_000_000_007;
5        int bits = 0;
6
7        for (int i = 1; i <= n; i ++) {
8            if ((i & (i - 1)) == 0 ) bits ++;
9            res = ((res << bits) | i) % MOD;
10        }
11
12
13        return (int) res;
14    }
15}
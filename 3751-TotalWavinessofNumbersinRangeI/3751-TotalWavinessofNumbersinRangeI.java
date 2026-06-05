// Last updated: 6/6/2026, 12:57:29 AM
1class Solution {
2    static final int[] waves = new int[570];
3
4    static {
5        int j = 0;
6        for (int i = 0; i < 1000; i++) {
7            int r = i % 10;
8            int m = (i / 10) % 10;
9            int l = (i / 100) % 10;
10            if ((m > Math.max(l, r)) | (m < Math.min(l, r)))
11                waves[j++] = i;
12        }
13    }
14
15    public long totalWaviness(long A, long B) {
16        return waveCount(B) - waveCount(A - 1);
17    }
18
19    private long waveCount(long num) {
20        if (num < 100) return 0;
21        long res = 0;
22        for (int p : waves)
23            res += countWays(num, p);            
24        return res;
25    }
26
27    private long countWays(long num, int pattern) {
28        long type = pattern < 100 ? 1 : 0;
29        long count = 0, mult = 1;
30
31        for (int i = 0; mult * 100 <= num; i++) {
32            long pre = num / (mult * 1000);
33            long cur = (num / mult) % 1000;
34            long suf = num % mult;
35            long ways = 0;
36
37            if (cur > pattern)
38                ways = pre - type + 1;
39            else if (cur == pattern) {
40                ways = Math.max(0L, pre - type);
41                count += suf + 1;
42            } else
43                ways = Math.max(0L, pre - type);
44
45            count += ways * mult;
46            mult *= 10;
47        }
48
49        return count;
50    }
51}
// Last updated: 2/14/2026, 1:27:48 AM
1class Solution {
2    public int longestBalanced(String s) {
3        int n = s.length();
4        int[] count = new int[26];
5        int res = 0;
6
7        for (int i = 0; i < n; i++) {
8            Arrays.fill(count, 0);
9            int max = 0;
10            int unique = 0;
11
12            for (int j = i; j < n; j++) {
13                int c = s.charAt(j) - 'a';
14
15                if (++count[c] == 1) {
16                    unique++;
17                }
18
19                max = Math.max(max, count[c]);
20
21                int length = j - i + 1;
22
23                if (max * unique == length) {
24                    res = Math.max(res, length);
25                }
26            }
27        }
28
29        return res;
30    }
31}
32
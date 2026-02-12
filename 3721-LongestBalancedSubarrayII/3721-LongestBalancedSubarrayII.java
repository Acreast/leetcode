// Last updated: 2/13/2026, 1:06:08 AM
1class Solution {
2    public int longestBalanced(String s) {
3        int n = s.length();
4        int res = 0;
5
6        for (int i = 0; i < n; i++) {
7            int[] count = new int[26];
8            int max = 0;
9            int unique = 0;
10
11            for (int j = i; j < n; j++) {
12                int c = s.charAt(j) - 'a';
13
14                if (++count[c] == 1) {
15                    unique++;
16                }
17
18                max = Math.max(max, count[c]);
19
20                int length = j - i + 1;
21
22                if (max * unique == length) {
23                    res = Math.max(res, length);
24                }
25            }
26        }
27
28        return res;
29    }
30}
31
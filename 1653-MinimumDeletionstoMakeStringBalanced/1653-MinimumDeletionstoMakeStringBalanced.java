// Last updated: 2/8/2026, 1:25:45 AM
1class Solution {
2    public int minimumDeletions(String s) {
3        int res = 0, b = 0;
4
5        for (int i = 0; i < s.length(); i++) {
6            char c = s.charAt(i);
7            if (c == 'b')
8                b++;
9            else if (b > 0) {
10                res++;
11                b--;
12            }
13        }
14
15        return res;
16    }
17}
18
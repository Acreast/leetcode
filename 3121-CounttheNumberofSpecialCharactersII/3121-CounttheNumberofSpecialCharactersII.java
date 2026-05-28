// Last updated: 5/29/2026, 12:36:13 AM
1class Solution {
2    public int numberOfSpecialChars(String word) {
3        boolean [][] A = new boolean[2][27];
4        for (int i = 0; i < word.length(); i ++) {
5            char ch = word.charAt(i);
6            int idx = ch & 31;
7            int Case = (ch >> 5) & 1;
8
9            A[Case][idx] = Case == 0 || !A[0][idx];
10        }
11
12        int res = 0;
13        for (int i = 1; i < 27; i ++) {
14            if (A[0][i] && A[1][i])
15                res ++;
16        }
17        return res;
18    }
19}
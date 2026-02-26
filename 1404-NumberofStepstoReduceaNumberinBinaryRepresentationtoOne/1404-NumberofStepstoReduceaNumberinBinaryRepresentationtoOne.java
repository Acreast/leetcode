// Last updated: 2/26/2026, 10:46:27 PM
1class Solution {
2    public int numSteps(String s) {
3        int carry = 0;
4        int res = 0;
5
6        for (int i = s.length() - 1; i != 0; i --) {
7            if ((s.charAt(i) & 1) + carry == 1) {
8                res += 2;
9                carry = 1;
10            } else {
11                res += 1;
12            }
13        }
14
15        return res + carry;
16    }
17}
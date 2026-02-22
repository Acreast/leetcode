// Last updated: 2/22/2026, 9:12:58 PM
1class Solution {
2    public int binaryGap(int n) {
3        String string_form_n = Integer.toBinaryString(n);
4        int prev_one_i = -1;
5        int res = 0;
6        for (int i = 0; i < string_form_n.length(); i ++) {
7            if (string_form_n.charAt(i) == '1') {
8                if (prev_one_i != -1) {
9                    res = Math.max(res, i - prev_one_i);
10                } 
11                prev_one_i = i;
12            }
13        } 
14        return res;
15    }
16}
// Last updated: 2/17/2026, 1:30:44 AM
1class Solution {
2    public int reverseBits(int n) {
3        int res = 0;
4        for (int i = 0; i < 32; i ++) {
5            res = (res << 1) | (n & 1);
6            n >>>= 1;
7        }
8
9        return res;
10    }
11}
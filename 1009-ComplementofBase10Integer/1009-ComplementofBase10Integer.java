// Last updated: 3/12/2026, 1:19:01 AM
1class Solution {
2    public int bitwiseComplement(int n) {
3        if (n == 0) return 1;
4        int bit_length = (int)(Math.log(n)/Math.log(2)) + 1;
5
6        int mask = (1 << bit_length) - 1;
7        return n ^ mask;
8    }
9}
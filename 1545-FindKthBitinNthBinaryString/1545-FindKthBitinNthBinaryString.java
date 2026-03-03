// Last updated: 3/3/2026, 11:57:32 PM
1class Solution {
2    public char findKthBit(int n, int k) {
3        int length = (int)Math.pow(2, n) - 1;
4        return helper(length, k);        
5    }
6
7
8    public static char helper(int length, int k) {
9        if (length == 1) {
10            return '0';
11        }
12
13        int half = length / 2;
14        if (k <= half) {
15            return helper(half, k);
16        } else if ( k > half + 1) {
17            int res = helper(half, 1 + length - k);
18            if (res == '1') {
19                return '0';
20            } else {
21                return '1';
22            }
23        } else {
24            return '1';
25        }
26
27    }
28}
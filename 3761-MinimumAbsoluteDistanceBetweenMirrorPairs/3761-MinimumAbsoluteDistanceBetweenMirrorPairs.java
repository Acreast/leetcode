// Last updated: 4/18/2026, 6:52:24 PM
1class Solution {
2    public int mirrorDistance(int n) {
3        int r = reverse(n);
4        return Math.abs(n - r);
5    }
6
7    private static int reverse(int num) {
8        int rev = 0;
9
10        while (num > 0) {
11            rev = rev * 10  + num % 10;
12            num /= 10;
13        }   
14
15        return rev;
16    }
17
18    
19}
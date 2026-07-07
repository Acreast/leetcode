// Last updated: 7/8/2026, 12:39:05 AM
1class Solution {
2    public long sumAndMultiply(int n) {
3        int cur = n;
4        long sum = 0;
5        long res = 0;
6        long multiplier = 1;
7        while ( cur != 0) {
8            int digit = cur % 10;
9            if (digit != 0) {
10                res = digit * multiplier + res; 
11                sum += digit;
12                multiplier *= 10; 
13            }
14            cur /= 10;
15        }
16        return res * sum;
17    }
18}
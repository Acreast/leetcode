// Last updated: 7/8/2026, 12:35:58 AM
1class Solution {
2    public long sumAndMultiply(int n) {
3        int cur = n;
4        int sum = 0;
5        int res = 0;
6        while ( cur != 0) {
7            int digit = cur % 10;
8            if (digit == 0) {
9                cur /= 10;
10                continue;
11            }
12                
13            res = res * 10 + digit;
14            sum = sum + digit;
15            cur /= 10;
16        }
17        long reversedRes = 0;
18        while (res > 0) {
19            reversedRes = reversedRes * 10 + (res % 10);
20            res /= 10;
21        }
22        return reversedRes * sum;
23    }
24}
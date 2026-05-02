// Last updated: 5/2/2026, 3:46:01 PM
1class Solution {
2    public int rotatedDigits(int n) {
3        int count = 0;
4        for (int i = 1; i <=n ; i ++) {
5
6            int num = i;
7            boolean is_valid = true;
8            boolean is_changed = false;
9
10            while (num > 0) {
11
12                int digit = num % 10;
13
14                if (digit == 3 || digit == 4 || digit == 7) {
15                    is_valid = false;
16                    break;
17                }
18
19                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
20                    is_changed = true;
21                }
22                num /= 10;
23            }
24            
25            if (is_valid && is_changed) {
26                count ++;
27            }
28
29        }
30
31        return count;
32    }
33}